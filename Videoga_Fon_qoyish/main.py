import cv2
import numpy as np
import matplotlib.pyplot as plt
video=cv2.VideoCapture(r'green3.mp4')
video2=cv2.VideoCapture(r'b.mp4')

out = cv2.VideoWriter('natija1.avi',cv2.VideoWriter_fourcc(*'DIVX'), 30, (1920,1080))
rasm_toplam = []
if not video.isOpened():
    print("Video yakunlandi")
    
while video.isOpened() and video2.isOpened():
    ret,frame=video.read()
    ret1,frame1=video2.read()
    
    
    if not (ret and ret1):
        break
    
    frame = cv2.resize(frame,(1920,1080),interpolation=cv2.INTER_LINEAR)
    frame1 = cv2.resize(frame1,(1920,1080),interpolation=cv2.INTER_LINEAR)
    frame_copy=np.copy(frame)
    
    lower_green=np.array([0,150,0])
    upper_green=np.array([150,255,150])
    
    mask=cv2.inRange(frame,lower_green,upper_green)
    
    frame_copy[mask!=0]=[0,0,0]
    
    frame1[mask==0]=[0,0,0]
    
    result=frame1+frame_copy
    rasm_toplam.append(result)
    cv2.imshow('Frame',result)
    
    if cv2.waitKey(1) & 0xFF==ord('q'):
        break
        
for i in rasm_toplam:
    out.write(i)
    
video2.release()
video.release()
out.release()
cv2.destroyAllWindows()
