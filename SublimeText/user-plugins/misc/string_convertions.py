
#convert string to hex
def toHex(s):
    lst = []
    for ch in s:
        hv = hex(ord(ch)).replace('0x', '')
        if len(hv) == 1:
            hv = '0'+hv
        lst.append(hv)
    
    return lst
    # return reduce(lambda x,y:x+y, lst)


def toDec(s):
    lst = []
    res = ''
    for ch in s:
        hv = ord(ch)
        res += str(hv) + ' '
        lst.append(hv)
    
    return res
    # return lst
    # return reduce(lambda x,y:x+y, lst)


#convert hex repr to string
def toStr(s):
  # return s and chr(atoi(s[:2], base=16)) + toStr(s[2:]) or ''  # python2
  return s and chr(int(s[:2], base=16)) + toStr(s[2:]) or ''
