import math

def nt(n):
    if n<2:
        return False
    for i in range(2,int(math.sqrt(n))+1):
        if n % i == 0:
            return False
    return True

n,m = map(int,input().split())
a = []
for i in range(n):
    b = [int(x) for x in input().split()]
    a.append(b)

for i in range(n):
    for j in range(m):
        if nt(a[i][j]):
            print(1,end=' ')
        else:
            print(0,end=' ')
    print()

