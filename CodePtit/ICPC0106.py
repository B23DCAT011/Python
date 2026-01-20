from math import log2



def toS(s):
    if s <=9: return str(s)
    return chr(ord('A')+s-10)

def convert(s):
    r = 0
    for i in s:
        r = r<<1 | int(i)
    return toS(r)

for _ in range(int(input())):
    b = int(log2(int(input())))
    s = input()
    r = ''
    while s!='':
        r = convert(s[-b:]) + r
        s = s[:-b]
    print(r)