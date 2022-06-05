from core.tools.buffer import AudioBuffer
from core.tools.pythonaudio import PyAudio
from core.utils.analysis import AnalyzeAudioStream as aas
from core.utils.constants import GUITAR_TUNING_FREQUENCY_MAPPING
import time

class Tuner():
    MIN_TARGET = 80
    MAX_TARGET = 1500
    CHUNK=4096
    RESOLUTION=44100
    BUFFER_LENGTH=2
    def __init__(self):
        self.pyaudio_client = PyAudio()
        self.buffer_obj = AudioBuffer(self.pyaudio_client)
        self.buffer_obj.start_audio_streaming()

    def listen_and_tune(self,tuning="E"):
        pass

    def stream_frequency(self,interval=0.25):
        start_time=0
        try:
            while True:
                data_chunk = self.pyaudio_client.stream_read(self.CHUNK)
                if (time.time()-start_time)>interval:
                    start_time=time.time()
                    freq = aas.get_frequency(data_chunk,self.CHUNK,self.RESOLUTION)
                    tuning_direction = self.get_relative_tuning(freq)
                    print(f"Frequency: {freq}")
        except: # pylint: disable=bare-except
            print("Error in stream.... closing now")
            return

    def get_relative_tuning(self, curr_freq):
        for target in GUITAR_TUNING_FREQUENCY_MAPPING["E"]:
            # Tuning logic
            pass

    def test_stream_frequency(self):
        self.buffer_obj.stream_to_buffer_and_get_freq()
