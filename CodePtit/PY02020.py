

n,a = int(input()), [float(x) for x in input().split()]

a = sorted(a)
min = a[0]
max = a[n-1]
sums= 0
cnt=0
for i in range(n):
    if a[i] == min or a[i]== max:
        a[i]=0
        cnt+=1
    sums += a[i]
print(round(sums/(len(a)-cnt),2))
