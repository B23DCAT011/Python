import math


def nt(n):
    if n < 2:
        return False
    for i in range(2,int(math.sqrt(n)+1)):
        if n%i == 0:
            return False
    return True

def check_index(s):
    for i in range(len(s)-1):
        if nt(i):
            if not nt(int(s[i])):
                return False
        else:
            if nt(int(s[i])):
                return False
    return True
for _ in range(int(input())):
    s = input()
    if check_index(s):
        print("YES")
    else:
        print("NO")


