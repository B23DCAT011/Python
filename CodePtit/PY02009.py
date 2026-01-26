

for _ in range(int(input())):
    n = int(input())
    a = {}
    for _ in range(n):
        x = int(input())
        if a.get(x): a[x]+=1
        else: a[x]=1
    a=sorted(a, key= lambda x : (-a[x],x))
    print(a[0])