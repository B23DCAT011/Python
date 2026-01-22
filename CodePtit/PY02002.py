arr = [0]
arr.append(1)

for i in range(2,93):
    arr.append(arr[i-1]+arr[i-2])
for _  in range(int(input())):
    a,b = map(int,input().split())
    for i in range(a,b+1):
        print(arr[i],end=' ')
    print()

