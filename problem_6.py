import zipfile, re, StringIO
from util import getFileData

zipFile = zipfile.ZipFile(StringIO.StringIO(getFileData('http://www.pythonchallenge.com/pc/def/channel.zip')))
files = zipFile.namelist()
nothing = re.findall('(?<=start from )[0-9]+', zipFile.open('readme.txt', 'r').read())[0]

comments = ''
while(True):
    try:
        fName = nothing + '.txt'
        s = zipFile.open(fName).read()
        nothing = re.findall('(?<=Next nothing is )[0-9]+', s)[0]
        comments += zipFile.getinfo(fName).comment
    except:
        print nothing, s
        break

print comments
