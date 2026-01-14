
p = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ_.'

def cout(x):
    return p.index(x)

while 1:
    s = input()
    if s[0]=='0': break
    k,str = s.split()
    #ans =  [p[(cout(x)+int(k))%28] for x in str]

    ans = []
    for items in str:
        ans.append(p[(cout(items)+int(k))%28])

    print(ans)
    print(''.join(reversed(ans)))
