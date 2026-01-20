import math


def sum_check(s):
    sums=0
    for i in s:
        sums+= int(i)
    return sums

def nt(n):
    if n < 2:
        return False
    for i in range(2,int(math.sqrt(n)+1)):
        if n%i == 0:
            return False
    return True

def check_index(s):
    for i in range(0,len(s)-1,2):
        if int(s[i])%2 == 1:
            return False
    for i in range(1,len(s)-1,2):
        if int(s[i])%2 == 0:
            return False
    return True
for _ in range(int(input())):
    s = input()
    if check_index(s) and nt(sum_check(s)):
        print("YES")
    else:
        print("NO")

