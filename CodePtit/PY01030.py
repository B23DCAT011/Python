import math

n,k = map(int,input().split())
arr = [x for x in range(10**(k-1),10**k) if math.gcd(x,n)==1]
for i in range(0,len(arr),10):
    print(' '.join([str(x) for x in arr[i:i+10]]))