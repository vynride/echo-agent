import pyaudio

def list_input_devices():
    pa = pyaudio.PyAudio()
    for i in range(pa.get_device_count()):
        dev = pa.get_device_info_by_index(i)
        if dev['maxInputChannels'] > 0:
            print(f"[{i}] {dev['name']}")
    pa.terminate()

list_input_devices()
