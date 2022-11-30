import time
import ultrasonic as dist

from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont

import Adafruit_SSD1306

def display_text(text, *args):

    if len(args) < 2:
        FONT_SIZE = 10
    elif len(args) == 2:
        FONT_SIZE = 9
    else:
        FONT_SIZE = 8

    disp = Adafruit_SSD1306.SSD1306_128_32(rst = 0)

    disp.begin()
    disp.clear()
    disp.display()

    width = disp.width
    height = disp.height

    # 1 bit pixel
    image = Image.new('1', (width, height))
    draw = ImageDraw.Draw(image)

    font = ImageFont.truetype("./ARIALUNI.TTF", FONT_SIZE)

    #try:
    #print('Press ^C to terminate')
    #   while True:

    draw.rectangle((0, 0, width, height), outline = 0, fill = 0)
            
    draw.text((0, 0), text, font = font, fill = 255)

    if len(args) > 0:
        for i, item in enumerate(args):
            draw.text((0, (i + 1) * FONT_SIZE-1), item, font = font, fill = 255)

    disp.image(image)
    disp.display()
    time.sleep(0.2)

    #except KeyboardInterrupt:
    #    print('terminated')

    #finally:
    #    disp.clear()
     #   disp.display()

if __name__ == "__main__":
    # display_text('一二三四五六七八九', '一二三四五六七八九', '一二三四五六七八九', '一二三四五六七八九')
    # display_text('玉樹臨風的整人專家', '中國古拳法傳人', '無敵風火輪')
    try:
        while True:
            d = dist.distance()
            display_text('Measured Distance = %.1f cm' %d)
            time.sleep(1)

    except KeyboardInterrupt:
        print("Measurement stopped by User")

