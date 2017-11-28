# Author: Aaron Renaghan
# Code Start Date: 25/10/2017

from moviepy.editor import *
import moviepy.editor as mp
import scipy.io.wavfile 
import numpy as np
import wave
import struct
import matplotlib.pyplot as plt

# Control Variables
writetofile = False
ourSampleRate = 100

# Video Clip Extraction
# Reads in Video
# Writes out Videos sounds into a .wav

chosenVideo = VideoFileClip("clips/Gbale.mp4")
temp_folder="clips/"
chosenVideo.audio.write_audiofile(temp_folder+"Sounds.wav")
waveFile = wave.open(temp_folder+"Sounds.wav")

# Getting details about the .wav file and prininting them out
no_channels = waveFile.getnchannels()
samp_width = waveFile.getsampwidth()
samp_freq = waveFile.getframerate()
length = waveFile.getnframes()

# Opening a text file to write out amplitudes
if writetofile == True:
	f = open('Amplitudes.txt', 'w')	

i = 0
highAmp = 0
highLight = 0

# While there are frames left to read 
while i < length:
    try:
		# Time can be figured out by dividing the frame number by the sampling rate
        time = i/samp_freq
		#reading in our data
        waveData = waveFile.readframes(1)
        data = struct.unpack("<i", waveData)
        s = str(int(data[0]))
		# Finding the highest value
        if data > highAmp:
            highAmp = data
            highlight = time
		# Printing progress
        frame = str(i)
        lengthTxt = str(length)
        print(frame + '/' + lengthTxt)
		# Writing Amplitudes to a file, This was to help understand the data
        if writetofile == True:
            s = str(int(data[0]))
            f.write('\nValue at Frame:')
            t = str(time)
            f.write('Time :')
            f.write(t)
            f.write(frame)
            f.write(' = ')
            f.write(s)
        i = i + ourSampleRate
    except ValueError:
        print('Value Error at line 125')
        break		

if writetofile == True:
	f.close()

	
# Printing Useful information
print "Number of Channels:", no_channels
print "Sample Width in Bytes;", samp_width
print "Sampling Frequency:", samp_freq
print "Number of Audio Frames:", length

print('Highest Amplitude Was')
print(highAmp)
print('Highest Amplitude Was At')
print(highlight)

# Writing out the highlight as a MP4
result = VideoFileClip(chosenVideo.filename).subclip(highlight-5,highlight+5)

result.write_videofile("Highlight.mp4",fps=25)
