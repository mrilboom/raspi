from PIL import Image
import LCD_2inch
import spidev as SPI
import logging
import io
import time
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
    path = ""
    #创建流
    for _, _, frames in os.walk(path):
        for frame in frames:
        image = Image.open(frame)
        disp.ShowImage(frame)
        time.sleep(0.05)
        
except IOError as e:
    disp.module_exit()
    logging.info(e)
except KeyboardInterrupt:
    disp.module_exit()
    logging.info("quit: KeyboardInterrupt")
    exit()