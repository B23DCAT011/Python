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

for _ in range(int(input())):
    string = input()
    sums = sum_check(string)
    if nt(sums):
        print("YES")
    else:
        print("NO")
