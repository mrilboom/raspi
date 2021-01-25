import io
import time
import picamera
from PIL import Image
import LCD_2inch
import spidev as SPI
import logging
#管角定义
RST = 27
DC = 25
BL = 18
bus = 0 
device = 0 
logging.basicConfig(level=logging.DEBUG)
# 创建流
stream = open('stream.jpg', 'wb')
with picamera.PiCamera() as camera:
    #设置像素和帧率
    camera.resolution = (240, 320)
    camera.framerate = 30
    camera.start_preview()
    #摄像头预热
    time.sleep(2)
    camera.capture(stream, format='jpeg')
# 将指针指向流的开始

#调用xxx.close来关闭流
try:
    # init
    disp = LCD_2inch.LCD_2inch()
    disp.Init()
    disp.clear()

    logging.info("show image")
    while True:
        image = Image.open(stream)
        disp.ShowImage(image)
except IOError as e:
    stream.close()
    disp.module_exit()
    logging.info(e)
except KeyboardInterrupt:
    stream.close()
    disp.module_exit()
    logging.info("quit: KeyboardInterrupt")
    exit()