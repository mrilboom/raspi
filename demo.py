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

try:
     # init
    disp = LCD_2inch.LCD_2inch()
    disp.Init()
    disp.clear()
    #创建流

    stream = io.BytesIO()
    with picamera.PiCamera() as camera:
        camera.resolution = (240, 320)
        camera.framerate = 15
        camera.start_preview()
        # 摄像头预热
        time.sleep(2)
        camera.capture(stream, 'jpeg')
        logging.info("show image")
        seq = 0
        while True:
            stream.seek(seq)
            image = Image.open(stream)
            disp.ShowImage(image)
            seq = seq + 1
except IOError as e:
    disp.module_exit()
    logging.info(e)
except KeyboardInterrupt:
    disp.module_exit()
    logging.info("quit: KeyboardInterrupt")
    exit()