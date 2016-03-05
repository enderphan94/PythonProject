import numpy as np
import cv2


cap = cv2.VideoCapture(0)

# Define the codec and create VideoWriter object
fourcc = cv2.VideoWriter_fourcc(*'XVID')
filename = "ender.avi"
flag = 0
incfilename = 1
out = cv2.VideoWriter(filename,fourcc, 20.0, (640,480))

while(cap.isOpened()):
    ret, frame = cap.read()
    if ret==True:
        
        print ('ender%s.avi' % str(incfilename))
        
        frame = cv2.flip(frame,1)

        # write the flipped frame
        
        out.write(frame)
        if flag >= 15:
            out.release()
            incfilename = incfilename + 1
            filename = "ender%s.avi" % str(incfilename)
            flag=0
            out = cv2.VideoWriter(filename,fourcc, 20.0, (640,480))
            out.write(frame)
            
            if incfilename==3:
                out.release()
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
