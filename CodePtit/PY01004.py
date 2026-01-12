import math
def gcd(a,b):
    if b==0:
        return a
    return gcd(b,a%b)


def nt(a):
    if a < 2:
        return 0
    for i in range(2,int(math.sqrt(a))+1):
        if a%i == 0:
            return 0
    return 1


t = int(input())
for i in range(t):
    n = int(input())
    k = 0
    for i in range(n):
        if gcd(i, n) == 1:
            k += 1

    if nt(k):
        print("YES")
    else:
        print("NO")

