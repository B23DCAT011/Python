import math


def tong_chu_so(x):
    return math.prod(int(c) for c in str(abs(x)))

for _ in range(int(input())):
    n = int(input())
    a = [int(x) for x in input().split()]

    a = sorted(a,key= lambda x : (tong_chu_so(x),x))
    for i in a:
        print(i,end=' ')
    print()
