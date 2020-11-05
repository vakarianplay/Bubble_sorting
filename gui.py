import cv2
import numpy as np
import os
os.environ["OPENCV_FFMPEG_CAPTURE_OPTIONS"] = "rtsp_transport;udp"
cap = cv2.VideoCapture("rtsp://admin:12345@192.168.10.198:554/10", cv2.CAP_FFMPEG)
cap2 = cv2.VideoCapture("rtsp://admin:12345@192.168.10.198:554/00", cv2.CAP_FFMPEG)

def rescale_frame(frame, percent=75):
    width = int(frame.shape[1] * percent/ 100)
    height = int(frame.shape[0] * percent/ 100)
    dim = (width, height)
    return cv2.resize(frame, dim, interpolation =cv2.INTER_AREA)
def rescale_frame2(frame2, percent=60):
    width = int(frame.shape[1] * percent/ 100)
    height = int(frame.shape[0] * percent/ 100)
    dim = (width, height)
    return cv2.resize(frame2, dim, interpolation =cv2.INTER_AREA)

while(1):
    rect, frame = cap.read()
    rect, frame2 = cap2.read()
    cam1 = rescale_frame(frame, percent=60)
    cam2 = rescale_frame2(frame2, percent=60)
    cv2.imshow('CAM1', cam1)
    cv2.imshow('CAM2', cam2)
    cv2.waitKey(1)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        cv2.destroyAllWindows()
        break

