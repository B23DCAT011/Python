


def solve(s):
    c=1
    l=0
    ok1=0
    ok2=0
    for i in range(len(s)):
        if i%2==1:
            l+= int(s[i])
        else:
            ok1+=1
            if s[i]!='0':
                c*=int(s[i])
            else:
                ok2+=1
    if ok1 == ok2:
        c=0
    return c,l

for _ in range(int(input())):
    s = input()
    c,l = solve(s)
    print(f'{c} {l}')

