# -*- coding: utf-8 -*-


#利用训练进行人脸识别
#同时云台控制
#Created By CxlDragon 2018.8.24

import cv2
import numpy as np
import os
from mysteer import *
import time

#+++++++++++++++++++++++
#云台初始化
# 13  # h 水平    # 26  # v 垂直
#初始位置为36和160，此时云台是正对前方，通过调试得到这两个值
#测试发现，垂直只能10-135，其它角度过了，水平5-160
#+++++++++++++++++++++++
steer=Steering(13,10,160,26,10,130,41,101) 
steer.setup()
time.sleep(2)
steer.specify(110,70)

#+++++++++++++++++++++++
#人脸识别初始化
#+++++++++++++++++++++++
font = cv2.FONT_HERSHEY_SIMPLEX
# 添加中文字体支持 /usr/share/fonts/truetype/wqy/wqy-zenhei.ttc
from PIL import Image, ImageDraw, ImageFont
cfont = ImageFont.truetype('wqy-zenhei.ttc', 40,encoding="utf-8") 
recognizer = cv2.face.LBPHFaceRecognizer_create()
recognizer.read('trainer/trainer.yml')
cascadePath = "haarcascade_frontalface_default.xml"
faceCascade = cv2.CascadeClassifier(cascadePath); 
#识别 id 计数器
id = 0 
# names related to ids: example ==> Marcelo: id=1,  etc
names = ['None', '龍龍發', '成成', 'ChengQY']  
# Initialize and start realtime video capture
cam = cv2.VideoCapture(0)
cam.set(3, 640) # set video widht
cam.set(4, 480) # set video height 
# Define min window size to be recognized as a face
minW = 0.1*cam.get(3)
minH = 0.1*cam.get(4)

#+++++++++++++++++++++++
#主程序
#+++++++++++++++++++++++
try:
    while True:
        ret, img =cam.read()
        #img = cv2.flip(img, -1) # 垂直旋转
        cv2.imshow('camera',img) #显示捕捉照片
        gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
        #人脸检测，参数用1.15，和采集时保持一致
        faces = faceCascade.detectMultiScale(
            gray,
            scaleFactor = 1.15,
            minNeighbors = 5,
            minSize = (int(minW), int(minH)),
            )
        #faces = faceCascade.detectMultiScale(gray, 1.15, 5)
     
        for(x,y,w,h) in faces:
            #print("检测到人脸")
            cv2.rectangle(img, (x,y), (x+w,y+h), (0,255,0), 2)
            id, confidence = recognizer.predict(gray[y:y+h,x:x+w])
       
            # Check if confidence is less them 100 ==> "0" is perfect match 
            if (confidence < 100):
                id = names[id]
                print("识别出"+str(id))
                confidence = "  {0}%".format(round(100 - confidence))
            else:
                id = "unknown"
                confidence = "  {0}%".format(round(100 - confidence))
             
            #cv2.putText(img, str(id), (x+5,y-5), font, 1, (255,255,255), 2)        
            #显示中文名字
            pil_im=Image.fromarray(img)
            draw =ImageDraw.Draw(pil_im)
            draw.text((x+5,y-50),str(id),(255,255,255),cfont)
            img=np.array(pil_im)
            #显示匹配度
            cv2.putText(img, str(confidence), (x+5,y+h-5), font, 1, (255,255,0), 1)
         
        cv2.imshow('camera',img) 
     
        k = cv2.waitKey(10) & 0xff #按键处理，退出，左右上下
        if k == 27:  #退出
            break
        elif k==75 : #左
            for i in range(0,50): #50表示一次10度
                steer.Left()
        elif k==77:  #右
            for i in range(0,50):
                steer.Right()
        elif k==72: #上
            for i in range(0,50):
                steer.Up()
        elif k==80:  #下
            for i in range(0,50):
                steer.Down()
        else:
            continue
        
finally:
    # Do a bit of cleanup
    print("\n [INFO] 退出程序，清理堆栈")
    steer.cleanup()
    cam.release()
    cv2.destroyAllWindows()
