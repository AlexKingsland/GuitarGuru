import numpy as np
import time
import matplotlib.pyplot as plt
from services.pythonaudio import PyAudio


class AudioBuffer():
    def __init__(self,pyaudio_client: PyAudio,chunk=4096,resolution=44100,buffer_length=2,verbose=True):
        """
        Instantiate audio buffer as a moving window of datapoints, that append and remove streamed 
        chunks retrieved from pyaudio lib handler
        """
        self.pyaudio_client=pyaudio_client
        self.chunk = chunk # number of data points to read at a time
        self.resolution = resolution # time resolution of the recording device (Hz)
        # for tape recording (continuous "tape" of recent audio)
        self.buffer_length=buffer_length #seconds
        # Instantiate tape
        self.buffer=np.empty(self.resolution*self.buffer_length)*np.nan
        self.verbose=verbose

    def start_audio_streaming(self):
        """
        Start streaming to buffer with pyaudio client
        """
        self.pyaudio_client.stream_start(self.resolution, self.chunk)

    def stop_audio_streaming(self):
        """
        Kill pyaudio streaming
        """
        self.pyaudio_client.stream_stop()

    def buffer_add(self):
        """add a single chunk to the tape."""
        self.buffer[:-self.chunk]=self.buffer[self.chunk:]
        self.buffer[-self.chunk:]=self.pyaudio_client.stream_read(self.chunk)

    def buffer_flush(self):
        """completely fill tape with new data."""
        reads_in_buffer=int(self.resolution*self.buffer_length/self.chunk)
        if self.verbose:
            print(f"flush {self.buffer_length}s buffer with {round(reads_in_buffer, 2)} ms reads")
        for _ in range(reads_in_buffer):
            self.buffer_add()

    def stream_to_buffer_and_plot(self,interval=.25):
        """ Listen to input stream, append/remove from tape, plot whats recorded on tape """
        start_time=0
        try:
            while True:
                self.buffer_add()
                if (time.time()-start_time)>interval:
                    start_time=time.time()
                    self.buffer_plot(None)
        except: # pylint: disable=bare-except
            print("Error in stream.... closing now")
            return

    def buffer_plot(self,filename="03.png"):
        """plot what's in the tape."""
        start_time=time.time()
        plt.plot(np.arange(len(self.buffer))/self.resolution,self.buffer)
        plt.axis([0,self.buffer_length,-2**16/2,2**16/2])
        if filename:
            plt.savefig(filename,dpi=50)
        else:
            plt.pause(0.05)
            plt.clf()
        if self.verbose:
            print(f"plotting interval: {round(((time.time()-start_time)*1000), 2)} ms")