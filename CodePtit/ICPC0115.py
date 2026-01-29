

def gt(x):
    if x==0: return 1
    return x*gt(x-1)

for _ in range(int(input())):
    s = input()
    sum = 0
    for x in s: sum+=gt(int(x))

    print("Yes" if int(s) == sum else "No")