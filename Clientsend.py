import socket

HOST = 'localhost'
PORT = 8000
ADDR = (HOST,PORT)
BUFSIZE = 5000
videofile = "D:/PythonProject/ender.avi"

bytes = open((videofile),"rb").read()

print len(bytes)

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(ADDR)

client.send(bytes)

client.close()
