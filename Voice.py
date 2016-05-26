import pyaudio
import math
import struct
import wave

#####################################################################
#         DEVELOPED BY ENDER - KUSTAS - CYBER SECURITY              #
#####################################################################

Threshold = 10
SHORT_NORMALIZE = (1.0/32768.0)
chunk = 1024
FORMAT = pyaudio.paInt16
CHANNELS = 1
RATE = 16000
swidth = 2
Max_Seconds =10
TimeoutSignals=((RATE / chunk * Max_Seconds) + 2)
silence = True
Time=0
incfilename=0



p = pyaudio.PyAudio()

stream = p.open(format = FORMAT,
    channels = CHANNELS,
    rate = RATE,
    input = True,
    output = True,
    frames_per_buffer = chunk)

def GetStream(chunk):
    stream = p.open(format = FORMAT,
    channels = CHANNELS,
    rate = RATE,
    input = True,
    output = True,
    frames_per_buffer = chunk)
    return stream.read(chunk)

#rms is root mean square, this is the value to compare with Threshold belonged to y-axis     

    
def rms(frame):   #root mean square
        count = len(frame)/swidth
    
        format = "%dh"%(count) #portion is calling for a single decimal value to become part of the string "count.h"
     
        shorts = struct.unpack( format, frame )
 
        sum_squares = 0.0
        for sample in shorts:
            n = sample * SHORT_NORMALIZE # 32byte to  SHORT_NORMALIZE megabyte
            #print n
            sum_squares += n*n
        rms = math.pow(sum_squares/count,0.5); #sqrt of sum_square
        #print rms * 1000
        return rms * 1000



def WriteSpeech(WriteData,incfilename):
    stream.stop_stream()
    stream.close()
    wf = wave.open("record%s.wav"%str(incfilename), 'wb')
    wf.setnchannels(CHANNELS)
    wf.setsampwidth(p.get_sample_size(FORMAT))
    wf.setframerate(RATE)
    wf.writeframes(WriteData)
    wf.close()

import time

def main(silence,incfilename):

    print "waiting for Speech"
    while True:
        stream = p.open(format = FORMAT,
    channels = CHANNELS,
    rate = RATE,
    input = True,
    output = True,
    frames_per_buffer = chunk)
    
    
        try:

            input = GetStream(chunk)

        except:

            continue
        
        rms_value = rms(input)
        print rms_value
        if (rms_value > Threshold):
            all =[]
            data = input
            count =0
            print "writing"
            for i in range (0, TimeoutSignals):
                
                data = GetStream(chunk)
                all.append(data)
                
                data = ''.join(all)
            
            
            WriteSpeech(data,incfilename)
            incfilename=incfilename + 1
   
    return

main(silence,incfilename)    



