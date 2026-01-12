t = int(input())

for i in range(t):
    n = list(input())
    lengths = len(n)
    memo = 0
    for i in range(1,lengths):
        x = int(n[lengths - i]) + memo
        if  x < 5:
            memo = 0
        else:
            memo = 1
        n[lengths - i] = '0'
    x = int(n[0]) + memo
    n[0] = str(x)
    for i in n:
        print(i, end="")
    print()

