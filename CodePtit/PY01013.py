import math


def check(n):
    if n < 2:
        return False
    for i in range(2,int(math.sqrt(n))+1):
        if(n%i==0):
            return False
    return True

t = int(input())

for i in range(t):
    a,b = map(int,input().split())
    c = math.gcd(a,b)
    sum_c = sum(int(ch) for ch in str(c))
    if(check(sum_c)):
        print("YES")
    else:
        print("NO")
