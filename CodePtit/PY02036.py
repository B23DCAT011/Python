import math

n,a = int(input()),[int(x) for x in input().split()]
a = sorted(a)
for i in range(len(a)):
    for j in range(i+1,len(a)):
        if math.gcd(a[i],a[j])==1:
            print(f'{a[i]} {a[j]}')