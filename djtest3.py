# -*- coding: UTF-8 -*-

from mysteer import *

import time
# 13  # h 水平
# 26  # v 垂直
#初始位置为36和160，此时云台是正对前方，通过调试得到这两个值
#测试发现，垂直只能10-135，其它角度过了，水平5-160
steer=Steering(13,10,160,26,10,130,41,101) 
steer.setup()
time.sleep(2)
'''
for i in range(0,900):
    steer.Up()

for i in range(0,900):
    steer.Down()

for i in range(0,900):
    steer.Left()

for i in range(0,900):
    steer.Right()
'''
#steer.specify(80,120)
steer.specify(50,100)
time.sleep(3)
steer.specify(110,50)

#控制
try:
    mystr=""
    try:
        while(True):
            time.sleep(1)
            mystr=input("请输入方向的数字（4-左 6-右 2-下 8-上 5-start 0-stop 其它－退出）：")
            con=int(mystr)
            if con==4 :
                for i in range(0,100): #50表示一次10度
                    steer.Left()
            elif con==6:
                for i in range(0,100):
                    steer.Right()
            elif con==8:
                for i in range(0,100):
                    steer.Up()
            elif con==2:
                for i in range(0,100):
                    steer.Down()
            elif con==5:  
                steer.start()
            elif con==0:
                steer.stop()
                
            else:
                break
    finally:
        print("退出循环守候")
        #退出
        steer.cleanup()
except ValueError:
    print("输入参数错误: "+mystr)
