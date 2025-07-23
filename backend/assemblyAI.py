import os
import pyaudio
import websocket
import json
import threading
import time
from urllib.parse import urlencode
from datetime import datetime
from pathlib import Path
from dotenv import load_dotenv


env_path = Path(__file__).parents[1] / ".env.local"
load_dotenv(env_path)


ASSEMBLY_API_KEY = os.environ.get("ASSEMBLY_API_KEY")


FRAMES_PER_BUFFER = 800  # 50ms of audio (0.05s * 16000Hz)
SAMPLE_RATE = 16000
CHANNELS = 1
FORMAT = pyaudio.paInt16
RATE=16000

CONNECTION_PARAMS = {
    "sample_rate": SAMPLE_RATE,
    "format_turns": True,
}


API_ENDPOINT_BASE_URL = "wss://streaming.assemblyai.com/v3/ws"
API_ENDPOINT = f"{API_ENDPOINT_BASE_URL}?{urlencode(CONNECTION_PARAMS)}"


audio = None
stream = None
ws_app = None
audio_thread = None
stop_event = threading.Event()

transcriptions = ""

def on_open(ws):
    global stop_event

    """Called when the WebSocket connection is established."""
    print("WebSocket connection opened.")
    print(f"Connected to: {API_ENDPOINT}")

    def stream_audio():
        global stream
        print("Starting audio streaming...")
        while not stop_event.is_set():
            try:
                audio_data = stream.read(FRAMES_PER_BUFFER, exception_on_overflow=False)
                
                ws.send(audio_data, websocket.ABNF.OPCODE_BINARY)
            except Exception as e:
                print(f"Error streaming audio: {e}")
                break
        print("Audio streaming stopped.")
    global audio_thread
    audio_thread = threading.Thread(target=stream_audio)
    audio_thread.daemon = (
        True
    )
    audio_thread.start()


def on_message(ws, message):
    global transcriptions

    try:
        data = json.loads(message)
        msg_type = data.get('type')
        if msg_type == "Begin":
            session_id = data.get('id')
            expires_at = data.get('expires_at')
            print(f"Session began: ID={session_id}, ExpiresAt={datetime.fromtimestamp(expires_at)}")
        elif msg_type == "Turn":

            transcript = data.get('transcript', '')
            formatted = data.get('turn_is_formatted', False)

            if formatted:
                transcriptions += (transcript + " ")

                print(f"\r{transcript}")
            else:
                print(f"\r{transcript}", end='')

        elif msg_type == "Termination":
            audio_duration = data.get('audio_duration_seconds', 0)
            session_duration = data.get('session_duration_seconds', 0)
            print(f"Session Terminated: Audio Duration={audio_duration}s, Session Duration={session_duration}s")
    except json.JSONDecodeError as e:
        print(f"Error decoding message: {e}")
    except Exception as e:
        print(f"Error handling message: {e}")


def on_error(ws, error):
    """Called when a WebSocket error occurs."""
    print(f"WebSocket Error: {error}")

    stop_event.set()


def on_close(ws, close_status_code, close_msg):

    """Called when the WebSocket connection is closed."""
    print(f"WebSocket Disconnected: Status={close_status_code}, Msg={close_msg}")
    
    global stream, audio, stop_event
    stop_event.set()
    if stream:
        if stream.is_active():
            stream.stop_stream()
        stream.close()
        stream = None
    if audio:
        audio.terminate()
        audio = None

    if audio_thread and audio_thread.is_alive():
        audio_thread.join(timeout=1.0)


def get_transcript():
    global audio, stream, ws_app, stop_event, transcriptions
    stop_event.clear()
    transcriptions = ""
    
    audio = pyaudio.PyAudio()
    try:
        stream = audio.open(
            format=pyaudio.paInt16,
            channels=CHANNELS,
            rate=SAMPLE_RATE,
            input=True,
            frames_per_buffer=FRAMES_PER_BUFFER,
            input_device_index=int(os.environ.get("PYAUDIO_INPUT_DEVICE"))
        )

        print("Microphone stream opened successfully.")
        print("Speak into your microphone. Press Ctrl+C to stop.")

    except Exception as e:
        print(f"Error opening microphone stream: {e}")

        if audio:
            audio.terminate()
        return

    ws_app = websocket.WebSocketApp(
        API_ENDPOINT,
        header={"Authorization": ASSEMBLY_API_KEY},
        on_open=on_open,
        on_message=on_message,
        on_error=on_error,
        on_close=on_close,
    )

    ws_thread = threading.Thread(target=ws_app.run_forever)
    ws_thread.daemon = True
    ws_thread.start()

    try:
        while ws_thread.is_alive() and not stop_event.is_set():
            time.sleep(0.1)

        if stop_event.is_set() and ws_app and ws_app.sock and ws_app.sock.connected:
            try:
                terminate_message = {"type": "Terminate"}
                print(f"Sending termination message: {json.dumps(terminate_message)}")
                ws_app.send(json.dumps(terminate_message))
                time.sleep(1)

            except Exception as e:
                print(f"Error sending termination message: {e}")

        if ws_app:
            try:
                ws_app.close()
            except:
                pass

        ws_thread.join(timeout=2.0)

    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        stop_event.set()
        if ws_app:
            try:
                ws_app.close()
            except:
                pass
        ws_thread.join(timeout=2.0)

    finally:

        if stream and stream.is_active():
            stream.stop_stream()
        if stream:
            stream.close()
        if audio:
            audio.terminate()
        print("Cleanup complete. Exiting.")

    return transcriptions
