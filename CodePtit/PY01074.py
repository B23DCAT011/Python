import math

sums=0
for _ in range(int(input())):
    n = int(input())
    cnt = 0
    for i in range(2,int(math.sqrt(n))+1):
        while n%i ==0:
            cnt+=i
            n/=i
    sums += cnt
    if n!= 1:
        sums+=n
print(int(sums))