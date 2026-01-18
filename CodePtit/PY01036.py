

t = int(input())

for _ in range(t):
    n = int(input())
    s = 0
    for i in range(n,0,-2):
        s+= 1/i
    print(f'{s:.6f}')