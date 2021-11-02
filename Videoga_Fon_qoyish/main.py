import cv2
import numpy as np
import matplotlib.pyplot as plt
video=cv2.VideoCapture(r'green.mp4')
video2=cv2.VideoCapture(r'b.mp4')

if not video.isOpened():
    print("Video yakunlandi")
    
while video.isOpened() and video2.isOpened():
    ret,frame=video.read()
    ret1,frame1=video2.read()
    
    if not (ret and ret1):
        break
    
    frame_copy=np.copy(frame)
    
    lower_green=np.array([0,160,0])
    upper_green=np.array([150,255,150])
    
    mask=cv2.inRange(frame,lower_green,upper_green)
    
    frame_copy[mask!=0]=[0,0,0]
    
    frame1[mask==0]=[0,0,0]
    
    result=frame1+frame_copy
    cv2.imshow('Frame',result)
    
    if cv2.waitKey(25) & 0xFF==ord('q'):
        break
    
video2.release()
video.release()
cv2.destroyAllWindows()
