#!/usr/bin/env python
import cv2


if __name__ == "__main__":
    # find the webcam
    capture = cv2.VideoCapture(0)

    # video recorder
    fourcc = cv2.VideoWriter_fourcc(*'XVID')   # cv2.VideoWriter_fourcc() does not exist
    video_writer = cv2.VideoWriter("output.mp4", fourcc, 20, (680, 480))

    # record video
    while (capture.isOpened()):
        ret, frame = capture.read()
        if ret:
            video_writer.write(frame)
            cv2.imshow('Video Stream', frame)

        else:
            break

capture.release()
video_writer.release()
cv2.destroyAllWindows()
