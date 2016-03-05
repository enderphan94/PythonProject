import io
import socket
import atexit
import numpy as np
import cv2


cap = cv2.VideoCapture(0)

# Define the codec and create VideoWriter object
fourcc = cv2.VideoWriter_fourcc(*'XVID')
out = cv2.VideoWriter('ender.avi',fourcc, 20.0, (640,480))
out2 = cv2.VideoWriter('ender2.avi',fourcc, 20.0, (640,480))
flag = 0


def camServer():

    while True:
        print("wait...")
        conn, addr = server_socket.accept()
        if conn:
            print(conn)
            print(addr)
            connection = conn.makefile('wb')
            break

    print("Connecting")
    try:
        while(cap.isOpened()):
   
            stream = io.BytesIO()
            camera.capture(stream, 'jpeg')
            stream.seek(0)
            connection.write(stream.read())
            stream.seek(0)
            stream.truncate()
            
            
    finally:
        print("close connection")
        connection.close()

def onExit():
    connection.close()
    server_socket.close()
    print("exit")


    server_socket = socket.socket()
    server_socket.bind(('10.59.1.255', 8000))
    server_socket.listen(0)
    server_socket.setblocking(1)
    
    while True:
        camServer()
