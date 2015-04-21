from PIL import Image
from util import getFileData
import StringIO

wire =  Image.open(StringIO.StringIO(getFileData('http://www.pythonchallenge.com/pc/return/wire.png'))).convert('RGB')
wirePixels = [wire.getpixel((i, 0)) for i in range(wire.size[0])]

squarePixels = [[None for i in range(100)] for i in range(100)]
x = 0
y = 0
i = 0

while i < len(wirePixels):
    while y < 100 and squarePixels[x][y] == None:
        squarePixels[x][y] = wirePixels[i]
        i += 1
        y += 1
    y -= 1
    x += 1
    
    while x < 100 and squarePixels[x][y] == None:
        squarePixels[x][y] = wirePixels[i]
        i += 1
        x += 1
    x -= 1
    y -= 1
    
    while y >= 0 and squarePixels[x][y] == None:
        squarePixels[x][y] = wirePixels[i]
        i += 1
        y -= 1
    y += 1
    x -= 1
    
    while x >= 0 and squarePixels[x][y] == None:
        squarePixels[x][y] = wirePixels[i]
        i += 1
        x -= 1
    x += 1
    y += 1

square = Image.new('RGB', (100, 100))
for x in range(100):
    for y in range(100):
        square.putpixel((x, y), squarePixels[x][y])
square.show()
