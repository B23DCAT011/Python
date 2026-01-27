n = int(input())
a = []

for i in range(n):
    b = [int(x) for x in reversed(input().split())]
    a.append(b)

sum1=sum2=0
for i in range(n):
    for j in range(n):
        if i > j: sum1+=a[i][j]
        if i< j : sum2+=a[i][j]
k = abs(sum1-sum2)
print("YES" if k <= int(input()) else "NO")
print(k)
