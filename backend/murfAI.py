import os
import datetime
import pyaudio
import wave
from pathlib import Path
from dotenv import load_dotenv
from murf import Murf

env_path = Path(__file__).parents[1] / ".env.local"
load_dotenv(env_path)

MURF_API_KEY = os.getenv("MURF_API_KEY")

def play_transcript(TRANSCRIPT, VOICEID, STYLE):
    client = Murf(api_key=MURF_API_KEY)
    res = client.text_to_speech.stream(text=TRANSCRIPT, voice_id=VOICEID, style=STYLE)

    ct = datetime.datetime.now()
    ct_str = ct.strftime("%Y-%m-%d %H-%M-%S")
    os.makedirs('murf_recordings', exist_ok=True)

    audio_data = b"".join(res)
    filename = f"murf_recordings/{ct_str}.wav"
    with wave.open(filename, 'wb') as wf:
        wf.setnchannels(1)
        wf.setsampwidth(2)
        wf.setframerate(44100)
        wf.writeframes(audio_data)

    chunk = 1024
    af = wave.open(filename, 'rb')
    pa = pyaudio.PyAudio()
    stream = pa.open(
        format=pa.get_format_from_width(af.getsampwidth()),
        channels=af.getnchannels(),
        rate=af.getframerate(),
        output_device_index=int(os.environ.get("PYAUDIO_OUTPUT_DEVICE")),
        output=True
    )

    rd_data = af.readframes(chunk)
    while rd_data:
        stream.write(rd_data)
        rd_data = af.readframes(chunk)

    stream.stop_stream()
    stream.close()
    pa.terminate()
