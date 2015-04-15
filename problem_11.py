import urllib2, StringIO, re, base64
from PIL import Image
request = urllib2.Request('http://www.pythonchallenge.com/pc/return/cave.jpg')
request.add_header('Authorization', 'Basic %s' % base64.encodestring('%s:%s' % ('huge', 'file')).replace('\n', ''))
image = Image.open(StringIO.StringIO(urllib2.urlopen(request).read())).convert('RGB')
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
