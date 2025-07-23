import pyaudio

def list_output_devices():
    pa = pyaudio.PyAudio()
    print("Available Output Devices:\n")
    for i in range(pa.get_device_count()):
        dev = pa.get_device_info_by_index(i)
        if dev['maxOutputChannels'] > 0:
            print(f"[{i}] {dev['name']} — Channels: {dev['maxOutputChannels']}")
    pa.terminate()
list_output_devices()
