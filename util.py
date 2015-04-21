import urllib2, base64

def getFileData(url, username = 'huge', password = 'file'):
    request = urllib2.Request(url)
    request.add_header('Authorization', 'Basic %s' % base64.encodestring('%s:%s' % (username, password)).replace('\n', ''))
    return urllib2.urlopen(request).read()
