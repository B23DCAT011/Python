

while True:
    a = [int(x) for x in input().split()]
    if a[0]==a[1]==a[2]==a[3]==0:
        break
    cnt = -1
    while True:
        cnt+=1
        if a[0]==a[1]==a[2]==a[3]:
            break
        tmp=a[0]
        for i in range(len(a)):
            if i==3:
                a[3] = abs(a[3]-tmp)
            else:
                a[i] = abs(a[i] - a[i + 1])
    print(cnt)
