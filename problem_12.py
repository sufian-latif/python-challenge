from util import getFileData
gfx = getFileData('http://www.pythonchallenge.com/pc/return/evil2.gfx')

ext = ['jpg', 'png', 'gif', 'png', 'jpg']
for i in range(5):
    s = 'img' + str(i) + '.' + ext[i]
    print s
    f = open(s, 'wb')
    f.write(gfx[i::5])
    f.close()
