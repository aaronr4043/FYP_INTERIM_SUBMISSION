# Author: Aaron Renaghan
# Code Start Date: 25/10/2017

from moviepy.editor import *
import moviepy.editor as mp
import scipy.io.wavfile 
import numpy as np
import wave
import struct
import matplotlib.pyplot as plt

# Video Clip Extraction

chosenVideo = VideoFileClip("clips/GBale.mp4")

temp_folder="clips/"

chosenVideo.audio.write_audiofile(temp_folder+"Sounds.wav")

waveFile = wave.open(temp_folder+"Sounds.wav")

#Getting details about the .wav file and prininting them out
no_of_channels = waveFile.getnchannels()
sample_width = waveFile.getsampwidth()
sample_freq = waveFile.getframerate()
number_frames = waveFile.getnframes()

print "Number of Channels:", no_of_channels
print "Sample Width in Bytes;", sample_width
print "Sampling Frequency:", sample_freq
print "Number of Audio Frames:", number_frames

f = open('workfile.txt', 'w')	

i = 0
highAmp = 0
highLight = 0

length = waveFile.getnframes()

while i < length:
    try:
        time = i/sample_freq
        waveData = waveFile.readframes(1)
        data = struct.unpack("<i", waveData)
        s = str(int(data[0]))
        if data > highAmp:
            highAmp = data
            highlight = time
        frame = str(i)
        lengthTxt = str(length)
        print(frame + '/' + lengthTxt)
        # f.write('\nValue at Frame:')
        # q = str(i)
        # t = str(time)
        # f.write('Time :')
        # f.write(t)
        # f.write(q)
        # f.write(' = ')
        # f.write(s)
        i = i + 100
    except ValueError:
        print('Value Error at line 125')
        break		
	
f.close()

print('Highest Amplitude Was')
print(highAmp)
print('Highest Amplitude Was At')
print(highlight)

chosenVideo = VideoFileClip("clips/GBale.mp4")

result = VideoFileClip("clips/GBale.mp4").subclip(highlight-5,highlight+5)

result.write_videofile("Highlight.mp4",fps=25)
