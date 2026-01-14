import math

for _ in range(int(input())):
    t = int(input())
    print(1,end='')
    for i in range(2,int(math.sqrt(t))+1):
        if(t%i==0):
            cnt = 0
            while(t%i==0):
                cnt+=1
                t/=i
            print(f' * {i}^{cnt}',end='')
    if(t>1):
        print(f' * {int(t)}^1',end='')
    print()