import numpy as np
import cv2


cap = cv2.VideoCapture(0)

# Define the codec and create VideoWriter object
fourcc = cv2.VideoWriter_fourcc(*'XVID')
out = cv2.VideoWriter('output1.avi',fourcc, 20.0, (640,480))
out2 = cv2.VideoWriter('output2.avi',fourcc, 20.0, (640,480))
flag = 0


while(cap.isOpened()):
   
    ret, frame = cap.read()
    if ret==True:
        frame = cv2.flip(frame,1)

        # write the flipped frameq
        
        if flag < 30:
            out.write(frame)
        if flag >= 30:
            out.release()
            out2.write(frame)
        if flag == 60:
            out2.release()
            break
            
        cv2.imshow('Ender Stream',frame)
        
        print flag
        flag = flag + 1
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    else:
        break

# Release everything if job is finished
cap.release()
#out.release()
cv2.destroyAllWindows()

def onExit():
    connection.close()
    server_socket.close()
    print("exit")

