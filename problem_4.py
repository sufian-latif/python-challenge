import urllib2
import re

def getNextNothing(nothing):
    try:
        s = urllib2.urlopen(url + nothing).read()
        return re.findall('and the next nothing is ([0-9]+)', s)[0]
    except:
        print s
        raise

def keepGoing(nothing):
    while(True):
        try:
            nothing = getNextNothing(nothing)
        except:
            break

url = 'http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing='
n = '12345'

keepGoing(n)
n = str(int(n) / 2)
keepGoing(n)
