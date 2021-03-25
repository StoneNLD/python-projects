#!/usr/bin/env python

from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont

def watermark_text(input_image_path, output_image_path, text, pos):
    photo = Image.open(input_image_path)
    # make the image editable
    drawing = ImageDraw.Draw(photo)
    black = (3, 8, 12)
    #MacOS local Fonts Lib
    font = ImageFont.truetype("/Library/Fonts/Arial", 100)
    drawing.text(pos, text, fill=black, font=font)
    photo.show()
    photo.save(output_image_path)

if __name__ == '__main__':
    img = 'image_104.jpg'
    watermark_text(img, 'watermark_text.jpg',
                   text='Watermarked!',
                   pos=(50, 50))