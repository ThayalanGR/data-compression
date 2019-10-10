import numpy as np
import matplotlib.pyplot as plt
from scipy.io.wavfile import read, write
from IPython.display import Audio
from numpy.fft import fft, ifft

# read audio input
Fs, data = read("./sample.wav")

data = data[:, 0]

print("sampling frequency is ", Fs)

Audio(data, rate=Fs)

plt.figure()
plt.plot(data)
plt.xlabel('SAMPLE INDEX')
plt.ylabel('AMPLITUDE')
plt.title('Waveform of Test Audio')
plt.show()

# write audio file
write('output.wav', Fs, data)