text = '''g fmnc wms bgblr rpylqjyrc gr zw fylb. rfyrq ufyr amknsrcpq ypc dmp. bmgle gr gl zw fylb gq glcddgagclr ylb rfyr'q ufw rfgq rcvr gq qm jmle. sqgle qrpgle.kyicrpylq() gq pcamkkclbcb. lmu ynnjw ml rfc spj.'''
print ''.join([chr(ord('a') + (ord(c) - ord('a') + 2) % 26) if c >= 'a' and c <= 'z' else c for c in text])

import string
tab = string.maketrans('abcdefghijklmnopqrstuvwxyz', 'cdefghijklmnopqrstuvwxyzab')
text2 = text.translate(tab)
print text2
print 'map'.translate(tab)
