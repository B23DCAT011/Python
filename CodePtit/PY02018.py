

n,a = int(input()) , [int(x) for x in input().split()]
a=sorted(a)
ok=0
for i in range(1,len(a)):
    if a[i]-a[i-1] > 1:
        ok=1
        print(a[i-1]+1)
        break
if ok==0:
    print(a[len(a)-1]+1)
