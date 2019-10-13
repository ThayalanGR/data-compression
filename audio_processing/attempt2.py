import math  # import needed modules
import pyaudio  # sudo apt-get install python-pyaudio

PyAudio = pyaudio.PyAudio  # initialize pyaudio

# See https://en.wikipedia.org/wiki/Bit_rate#Audio
BITRATE = 16000  # number of frames per second/frameset.

FREQUENCY = 500  # Hz, waves per second, 261.63=C4-note.
LENGTH = 1  # seconds to play sound

inputData = list('68656C6C6F20776F726C64')
print(inputData)

if FREQUENCY > BITRATE:
    BITRATE = FREQUENCY+100

NUMBEROFFRAMES = int(BITRATE * LENGTH)
RESTFRAMES = NUMBEROFFRAMES % BITRATE
WAVEDATA = ''

print(BITRATE, FREQUENCY)

# generating wawes
for x in inputData:
    print("ord", ord(x))
    val = math.sin(ord(x)/((BITRATE/FREQUENCY)/math.pi))
    print(val)
    val = val*127
    print(val)
    val = val+128
    print("sin", val)
    op = val - 128
    print("opp", op)
    op = op/127
    print("opp", op)
    op = math.asin(op)*((BITRATE/FREQUENCY)/math.pi)
    print("opp", op)
    # print("recover", math.asin((val-128)/127)*((BITRATE/FREQUENCY)/math.pi))

    WAVEDATA = WAVEDATA + \
        chr(int(math.sin(ord(x)/((BITRATE/FREQUENCY)/math.pi))*127+128))

# for x in range(RESTFRAMES):
#     WAVEDATA = WAVEDATA+chr(128)

p = PyAudio()
stream = p.open(format=p.get_format_from_width(1),
                channels=1,
                rate=BITRATE,
                output=True)

stream.write(WAVEDATA)
stream.stop_stream()
stream.close()
p.terminate()
