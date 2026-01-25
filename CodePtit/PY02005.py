n = int(input())
b = [int(x) for x in input().split()]
ans = 0


for i in range(n):
    for j in range(i+1,n):
        if b[j]<b[i]:ans+=1

print(ans)
