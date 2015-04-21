import StringIO, re
from PIL import Image
from util import getFileData
image = Image.open(StringIO.StringIO(getFileData('http://www.pythonchallenge.com/pc/return/cave.jpg'))).convert('RGB')
pixels = image.load()
width, height = image.size

image1 = Image.new('RGB', (width / 2, height / 2))
image2 = Image.new('RGB', (width / 2, height / 2))
pixels1, pixels2 = image1.load(), image2.load()

for x in range(width):
    for y in range(height):
        if (x + y) % 2 == 0:
            pixels1[x / 2, y / 2] = pixels[x, y]
        else:
            pixels2[x / 2, y / 2] = pixels[x, y]

image1.show()
