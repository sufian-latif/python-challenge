import urllib2, StringIO, re
from PIL import Image
image = Image.open(StringIO.StringIO(urllib2.urlopen('http://www.pythonchallenge.com/pc/def/oxygen.png').read()))
image = image.convert('RGB')
height = image.size[1]
s = ''.join([chr(image.getpixel((i, height / 2))[0]) for i in range(0, image.size[0], 7)])
nums = re.findall('[0-9]+', s)
print ''.join([chr(int(n)) for n in nums])
