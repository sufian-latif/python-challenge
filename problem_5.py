import pickle, urllib2
print '\n'.join([''.join([item[0] * item[1] for item in row]) for row in
                 pickle.load(urllib2.urlopen('http://www.pythonchallenge.com/pc/def/banner.p'))])
