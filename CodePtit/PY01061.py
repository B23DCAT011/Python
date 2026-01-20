from math import sqrt


def nt(n):
    if n < 2:
        return False
    for i in range(2,int(sqrt(n)+1)):
        if n%i == 0:
            return False
    return True

for _ in range(int(input())):
    s = input()
    if nt(int(s[:3])) and nt(int(s[-3:])):
        print("YES")
    else:
        print("NO")
