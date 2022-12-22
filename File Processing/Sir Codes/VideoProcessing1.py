import cv2

#1.Reading from Video File

cap=cv2.VideoCapture('short.mp4')
while True:
  ret,frame=cap.read()
  #frame=cv2.resize(frame,(200,200))
  gray=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
  cv2.imshow('Window Name',gray)
  #cv2.imshow('Gray',gray)
  k=cv2.waitKey(15)   #playback speed 15 or particular no. of frames in 15 ms . No.of frames is fixed per second...we are just changing denominator.If we increase it, speed will decrease
  if k==ord('q'):
    break
  
cap.release()
cv2.destroyAllWindows()

























'''

#2.Reading from Webcam
cap=cv2.VideoCapture(0)     #cap=cv2.VideoCapture(1)   cap=VideoCapture(0,cv2.CAP_DSHOW)
while cap.isOpened():
  ret,frame=cap.read()
  if ret==True:
    frame=cv2.resize(frame,(200,200))
    gray=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    cv2.imshow('Window Name',frame)
    cv2.imshow('Gray',gray)
    k=cv2.waitKey(15)   #playback speed 15 or particular no. of frames in 15 ms . No.of frames is fixed per second...we are just changing denominator.If we increase it, speed will decrease
    if k==ord('q'):
      break
    
cap.release()
cv2.destroyAllWindows()


#3. Writing Video to the file

obj=cv2.VideoWriter_fourcc(*'XVID')                  #codec
#XVID,DIVX,MJPG,X264,WMV1,WMV2
output1=cv2.VideoWriter('videocreatedcolored.mp4',obj,25,(854,480))     #file,codec,fps,resolution  by deafult last parameter is 1 for colored image
output2=cv2.VideoWriter('videocreatedgray.mp4',obj,25,(854,480),0)  
#VideoWriter('videocreated.avi',obj,20,(400,400),0) for writing grayscale image
cap=cv2.VideoCapture('short.mp4')     #cap=cv2.VideoCapture(1)   cap=VideoCapture(0,CAP_DSHOW)
while True:
  ret,frame=cap.read()
  if ret==True:
    #frame=cv2.resize(frame,(200,200))
    gray=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    output1.write(frame)
    output2.write(gray)
    #cv2.imshow('Window Name',frame)
    #cv2.imshow('Gray',gray)
    k=cv2.waitKey(15)   #playback speed 15 or particular no. of frames in 15 ms . No.of frames is fixed per second...we are just changing denominator.If we increase it, speed will decrease
    if k==ord('q'):
      break
    print('PROCESSING')
  else:
    break
print('COMPLETED')
output1.release()
output2.release()
cap.release()
cv2.destroyAllWindows()


#4. Connect Android Mobile camera to opencv

url="IPaddress/video"            #IP address of Android App and Internet
cap=cv2.VideoCapture(0)
cap.open(url)
Rest part is same as above

#5. Connect Youtube Video to opencv
'''
'''
import pafy                                        #install pafy,youtube_dl==2020.12.2
url=r"https://www.youtube.com/watch?v=H9154xIoYTA"
data=pafy.new(url)
data=data.getbest(preftype='mp4')
cap=cv2.VideoCapture(0)
cap.open(data.url)

while cap.isOpened():
  ret,frame=cap.read()
  if ret==True:
    frame=cv2.resize(frame,(200,200))
    gray=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    cv2.imshow('Window Name',frame)
    cv2.imshow('Gray',gray)
    k=cv2.waitKey(15)   
    if k==ord('q'):
      break
    
cap.release()
cv2.destroyAllWindows()








'''


















