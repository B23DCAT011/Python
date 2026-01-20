from math import sqrt

def nt(n):
    if n < 2:
        return False
    for i in range(2,int(sqrt(n)+1)):
        if n%i == 0:
            return False
    return True

for _ in range(int(input())):
    # print(int(input())**2)
    s = input()
    cnt = 0
    n = len(s)
    for i in range(n):
        if nt(int(s[i])):
            cnt+=1
    if nt(n) and cnt > len(s)-cnt:
        print("YES")
    else:
        print("NO")


