import numpy as np

class AnalyzeAudioStream:

	@staticmethod
	def get_frequency(buffer_chunk,chunk_size,rate):
		fft = abs(np.fft.fft(buffer_chunk).real)
		freq = np.fft.fftfreq(chunk_size,1.0/rate)
		peak_freq = np.abs(freq[np.where(fft==np.max(fft))])
		return peak_freq[0]

	@staticmethod
	def apply_filter(buffer_chunk):
		pass

	@staticmethod
	def apply_fft(buffer_chunk):
		pass