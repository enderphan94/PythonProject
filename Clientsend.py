import socket
import os
import schedule
import time
import thread

#####################################################################
#         DEVELOPED BY ENDER - KUSTAS - CYBER SECURITY              #
#####################################################################

HOST = 'localhost'
PORT = 8080
ADDR = (HOST,PORT)
BUFSIZE = 5000


incfilename=0

while True:
   
    try:        
        #if(os.path.exists(filename)):
        incfilename = incfilename + 1
        #filename = "picture%s.jpg" % str(incfilename)
        
        #soundname = "sound%s.wav" % str(incfilename)
        
        imagefile = "D:/PythonProject/xampp/picture%s.jpg"% str(incfilename)
        
        read_image = open(imagefile,"rb").read()

        soundfile = "D:/PythonProject/xampp/record%s.wav"% str(incfilename)
        
        read_sound = open((soundfile),"rb").read()
        
        client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        client.connect(ADDR)
        client.send("hi server")
        client.send(read_image)
        client.send(read_sound)
    except:
        time.sleep(5)
        print "hello "
    
    




