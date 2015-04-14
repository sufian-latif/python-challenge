def selfDescSeq(n):
    if n == 0:
        return '1'
    prev = selfDescSeq(n - 1)
    s = ''
    i = 0
    while i < len(prev):
        j = i
        while j < len(prev) and prev[j] == prev[i]:
            j += 1
        s += str(j - i) + prev[i]
        i = j
    return s

print len(selfDescSeq(30))
