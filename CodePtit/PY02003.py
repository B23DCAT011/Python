a = set()
max = int(1e18)

for i in range(65):
    n1 = 2**i # 1<<i
    if n1 > max :break
    for j in range(40):
        n2 = 3**j
        if n1*n2 > max:break
        for k in range(28):
            n3 = 5**k
            if n1*n2*n3>max:break
            a.add(n1*n2*n3)
a = sorted(a)

def bs(l,r,v):
    if l>r: return 'Not in sequence'
    mid = (l+r)>>1
    if a[mid] == v: return mid+1
    if a[mid] < v: return bs(mid+1,r,v)
    return bs(l,mid-1,v)

for t in range(int(input())):
    print(bs(0,len(a),int(input())))