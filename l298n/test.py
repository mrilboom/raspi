import RPi.GPIO as GPIO
import time
import keyboard

#编码方式
GPIO.setmode(GPIO.BOARD)


#输入编码 分别对应GPIO 22、26、23、24
IN1 = 31
IN2 = 32
IN3 = 33
IN4 = 35


def init():
    GPIO.setup(IN1,GPIO.OUT)
    GPIO.setup(IN2,GPIO.OUT)
    GPIO.setup(IN3,GPIO.OUT)
    GPIO.setup(IN4,GPIO.OUT)

'''
L298N模块IN1、IN2和IN1、IN2分别对应两个马达，输出IN1>IN2为前进，IN1<IN2为后退
pwm调速暂未启用
树莓派和l298n必须公地，否则无法启动！
'''
def forward():
    GPIO.output(IN1,GPIO.HIGH)
    GPIO.output(IN2,GPIO.LOW)
    GPIO.output(IN3,GPIO.HIGH)
    GPIO.output(IN4,GPIO.LOW)


def backward():
    GPIO.output(IN1,GPIO.LOW)
    GPIO.output(IN2,GPIO.HIGH)
    GPIO.output(IN3,GPIO.LOW)
    GPIO.output(IN4,GPIO.HIGH)


def left():
    GPIO.output(IN1,False)
    GPIO.output(IN2,False)
    GPIO.output(IN3,GPIO.HIGH)
    GPIO.output(IN4,GPIO.LOW)


def right():
    GPIO.output(IN1,GPIO.HIGH)
    GPIO.output(IN2,GPIO.LOW)
    GPIO.output(IN3,False)
    GPIO.output(IN4,False)

try:
    init()
    while True:
        if keyboard.is_pressed('w'):
            print('Forward')
            forward()
        elif keyboard.is_pressed('s'):
            print('Backward')
            backward()
        elif keyboard.is_pressed('a'):
            print('Left')
            left()
        elif keyboard.is_pressed('d'):
            print('Right')
            right()
        elif keyboard.is_pressed('q'):
            print('Quit!')
except:
    GPIO.cleanup()
    print("error...")