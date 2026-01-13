

def check(n):
    n = str(n)
    if(len(n) %2 == 1):
        return False
    if( n != n[::-1]):
        return False
    for item in n:
        if(int(item) % 2 ==1):
            return False
    return True

t = int(input())

for i in range(t):
    n = int(input())
    for i in range(n):
        if check(i):
            print(i,end=" ")
    print()