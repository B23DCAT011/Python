


t = int(input())

for j in range(t):
    n,x,m = map(float,input().split())
    cnt = 0
    while(True):
        n = n + n*x/100
        cnt+=1
        if(n >= m):
            break
    print(cnt)


