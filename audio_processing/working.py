import math
import wave
import struct


def make_sine(freq=440, datasize=10000, fname="test.wav", framerate=44100.00):
    amp = 8000.0  # amplitude
    for x in inputData:
        # sine generation code
        ordx = float("0."+str(ord(x)))
        a = 2 * math.pi * freq * (ordx/frate)
        temp = math.sin(a)
        sine_list.append(temp)
        # recover code
        atemp = (math.asin(temp) * frate) / (2 * math.pi * freq)
        rd = int(str(round(atemp, 2)).split(".")[1])
        recoverdData.append(chr(rd if(len(str(rd)) == 2) else rd * 10))

    # Open up a wav file
    wav_file = wave.open(fname, "w")
    # wav params
    nchannels = 1
    sampwidth = 2
    framerate = frate
    nframes = datasize
    comptype = "NONE"
    compname = "not compressed"
    wav_file.setparams((nchannels, sampwidth, framerate,
                        nframes, comptype, compname))
    # write on file
    for s in sine_list:
        wav_file.writeframes(struct.pack('h', int(s*amp/2)))
    wav_file.close()


inputData = list('68656C6C6F20776F726C64')
sine_list = []
recoverdData = []
frate = 44100  # that's the framerate
freq = 987.0  # that's the frequency, in hertz
seconds = 3  # seconds of file
data_length = frate*seconds  # number of frames
fname = "working.wav"  # name of file
make_sine(freq, data_length, fname)
print("inputData", inputData)
print("recoverdData", recoverdData)
