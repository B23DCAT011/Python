import math


def nt(n):
    if n<2:
        return False
    for i in range(2,int(math.sqrt(n))+1):
        if n % i == 0:
            return False
    return True

n,a = int(input()), [int(x) for x in input().split()]
m = {}

for x in a:
    if(nt(x)):
        try: m[x]+=1
        except: m[x]=1

for x in m:
    print(x,m[x],sep=' ')
