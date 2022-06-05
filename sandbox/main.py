# import core.tools 
# import AudioBuffer
# from core.tools.pythonaudio import PyAudio
from core.applications.tuner import Tuner
import sys

def main():
    """
    Test Pipelines
    """
    # pyaudio_obj = PyAudio()
    # buffer_obj = AudioBuffer(pyaudio_obj)
    # buffer_obj.start_audio_streaming()
    # buffer_obj.stream_to_buffer_and_plot()
    # buffer_obj.stop_audio_streaming()
    tuner = Tuner()
    tuner.stream_frequency()


if __name__ == "__main__":
    main()
