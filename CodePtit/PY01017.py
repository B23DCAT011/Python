

t = int(input())

for _ in range(t):
    string = list(input())
    cnt = 1
    for i in range(1,len(string)):

        if(string[i]==string[i-1]):
            cnt+=1
        else:
            print(f"{cnt}{string[i-1]}",end="")
            cnt = 1
    print(cnt,end='')
    print(string[len(string)-1])