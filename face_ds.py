import cv2
#import os
 
cam = cv2.VideoCapture(0)
cam.set(3, 640) # set video width
cam.set(4, 480) # set video height
 
face_detector = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
 
# For each person, enter one numeric face id
face_id = input('\n 请输入待采集的用户ID然后按下<回车键> ==>  ')
 
print("\n [INFO] 初始化摄像头，请看着摄像头并稍后 ...")
# Initialize individual sampling face count
count = 0
 
while(True):
    ret, img = cam.read()
    img = cv2.flip(img, -1) # flip video image vertically
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    faces = face_detector.detectMultiScale(gray, 1.3, 5)
 
    for (x,y,w,h) in faces:
        cv2.rectangle(img, (x,y), (x+w,y+h), (255,0,0), 2)     
        count += 1   #count=count +1
        print("检测到人脸-"+str(count))
 
        # Save the captured image into the datasets folder
        cv2.imwrite("dataset/User." + str(face_id) + '.' + str(count) + ".jpg", gray[y:y+h,x:x+w])
        cv2.imshow('image', img)
 
    k = cv2.waitKey(100) & 0xff # Press 'ESC' for exiting video
    if k == 27:
        break
    elif count >= 30: # 拍照够30张停止并退出
         break
 
# Do a bit of cleanup
print("\n [INFO] 退出并清理")
cam.release()
cv2.destroyAllWindows()
