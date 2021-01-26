import RPi.GPIO as GPIO
import time


#编码方式
GPIO.setmode(GPIO.BOARD)


#输入编码 分别对应GPIO 22、26、23、24
IN1 = 31
IN2 = 32
IN3 = 33
IN4 = 35


def init()
    GPIO.setup(IN1,GPIO.OUT)
    GPIO.setup(IN2,GPIO.OUT)
    GPIO.setup(IN3,GPIO.OUT)
    GPIO.setup(IN4,GPIO.OUT)

'''
L298N模块IN1、IN2和IN1、IN2分别对应两个马达，输出IN1>IN2为前进，IN1<IN2为后退
pwm调速暂未启用
'''
def forward()
    GPIO.output(IN1,GPIO.HIGH)
    GPIO.output(IN2,GPIO.LOW)
    GPIO.output(IN3,GPIO.HIGH)
    GPIO.output(IN4,GPIO.LOW)
    time.sleep(2)
    GPIO.cleanup()


def backward()
    GPIO.output(IN1,GPIO.LOW)
    GPIO.output(IN2,GPIO.HIGH)
    GPIO.output(IN3,GPIO.LOW)
    GPIO.output(IN4,GPIO.HIGH)
    time.sleep(2)
    GPIO.cleanup()


def left():
    GPIO.output(IN1,False)
    GPIO.output(IN2,False)
    GPIO.output(IN3,GPIO.HIGH)
    GPIO.output(IN4,GPIO.LOW)
    time.sleep(2)
    GPIO.cleanup()
 

def right():
    GPIO.output(IN1,GPIO.HIGH)
    GPIO.output(IN2,GPIO.LOW)
    GPIO.output(IN3,False)
    GPIO.output(IN4,False)
    time.sleep(2)
    GPIO.cleanup()

init()
print("moving")
forward()
print("success")