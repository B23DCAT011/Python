import math


for t in range(int(input())):
    def nt(n):
        if n<2: return 'NO'
        for i in range(2,int(math.sqrt(n))+1):
            if n%i==0: return False
        return True
    def ans(n):
        if not (nt(len(n))): return "NO"
        nto = [x for x in n if nt(int(x))]
        return "YES" if len(nto)>len(n)-len(nto) else "NO"

    print(ans(input()))

