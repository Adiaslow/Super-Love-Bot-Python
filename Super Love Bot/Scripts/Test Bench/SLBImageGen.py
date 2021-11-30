import random
import matplotlib.pyplot as plt
from PIL import Image, ImageDraw, ImageFont, ImageColor
import re
import time

# genorates random hex
number_of_colors = 2

BGHexColor = ("#"+''.join([random.choice('0123456789ABCDEF') for j in range(6)]))
print(BGHexColor)

textHexColor = ("#"+''.join([random.choice('0123456789ABCDEF') for j in range(6)]))
print(textHexColor)

colors = [BGHexColor, textHexColor]

# plots colors
for i in range(number_of_colors):
    plt.scatter(random.randint(0, 10), random.randint(0,10), c=colors[i], s=200)

plt.show()

# converts hex to RGB
BGRGBColor = ImageColor.getrgb(BGHexColor)
print(BGRGBColor)

textRGBColor = ImageColor.getrgb(textHexColor)
print(textRGBColor)

# recieves message
msg = "Wove coul\nnove to\nthe wis\nson the\nlove cave, er\nlove."

# creates image

whiteText = True

W, H = (1080, 1080)

if whiteText == False:
    textRGBColor = textRGBColor
    
elif whiteText == True:
    textRGBColor = (256, 256, 256)
    
img = Image.new('RGB', (W, H), color = (BGRGBColor))
 
fnt = ImageFont.truetype('/Library/Fonts/Hack-Regular.ttf', 150)
d = ImageDraw.Draw(img)
w, h = d.textsize(msg)
d.text((100, 100), msg, font=fnt, fill=(textRGBColor))

# date = 
 
img.save('pil_text_font.png')
