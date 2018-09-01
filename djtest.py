#-*- coding:UTF-8 -*-
#本次舵机转动控制七彩灯控制舵机采用的是系统的pwm库
import RPi.GPIO as GPIO
import time

#舵机引脚定义
#ServoPin = 13  #左右
#ServoPin = 26  #上下
vPin = 26  #垂直
hPin = 13  #水平

#设置GPIO口为BCM编码方式
GPIO.setmode(GPIO.BCM)

#忽略警告信息
GPIO.setwarnings(False)

#舵机引脚设置为输出模式
def init():
    global pwm_vser,pwm_hser
    #设置pwm引脚和频率为50hz
    #v    
    GPIO.setup(vPin, GPIO.OUT)
    #设置pwm引脚和频率为50hz
    pwm_vser = GPIO.PWM(vPin, 100)
    pwm_vser.start(0)
    #h
    GPIO.setup(hPin, GPIO.OUT)
    #设置pwm引脚和频率为50hz
    pwm_hser = GPIO.PWM(hPin, 100)
    pwm_hser.start(0)

#v 上下转
def vser_control():
    for pos in range(50,150):
        pwm_vser.ChangeDutyCycle(2.5 + 10 * pos/180)
        time.sleep(0.03)
    time.sleep(2)
    for pos in reversed(range(50,150)):
        pwm_vser.ChangeDutyCycle(2.5 + 10 * pos/180)
        time.sleep(0.03)
        
#h 左右转
def hser_control():
    for pos in range(50,150):
        pwm_hser.ChangeDutyCycle(2.5 + 10 * pos/180)
        time.sleep(0.03)
    time.sleep(2)
    for pos in reversed(range(50,150)):
        pwm_hser.ChangeDutyCycle(2.5 + 10 * pos/180)
        time.sleep(0.03)

#延时2s		
time.sleep(2)

#try/except语句用来检测try语句块中的错误，
#从而让except语句捕获异常信息并处理。
try:
    init()
    #舵机初始化向前
    #pwm_vser.ChangeDutyCycle(2.5 + 10 * 90/180)
    #pwm_hser.ChangeDutyCycle(2.5 + 10 * 90/180)
    #while True:
    vser_control()
    hser_control()
    time.sleep(5)
    vser_control()
    hser_control()    

except KeyboardInterrupt:
    pass
pwm_vser.stop()
pwm_hser.stop()
GPIO.cleanup()
