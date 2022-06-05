import pyaudio
import numpy as np
from core.tools.buffer import AudioBuffer

class PyAudio():
    def __init__(self,verbose=True):
        """
        instantiate pyaudio client and buffer for input stream recording to plot
        """
        self.input_stream = None # on start will beinput stream from mic via pyaudio

        self.client=pyaudio.PyAudio()

        self.verbose=verbose

    def stream_read(self,chunk):
        """
        return values for a single chunk
        """
        data = np.frombuffer(self.input_stream.read(chunk),dtype=np.int16)
        return data

    def stream_start(self,rate,chunk):
        """
        start audio input stream
        """
        if self.verbose:
            print(" -- stream started")
        self.input_stream=self.client.open(format=pyaudio.paInt16,channels=1,
                                rate=rate,input=True,
                                frames_per_buffer=chunk)

    def stream_stop(self):
        """
        close the stream but keep the PyAudio instance alive.
        """
        self.input_stream.stop_stream()
        self.input_stream.close()
        if self.verbose:
            print("Programatically closing stream")
