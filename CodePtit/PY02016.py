



for _ in range(int(input())):
    n = int(input())
    a = [int(x) for x in input().split()]
    m = {}

    def cnt(m):
        for i in m:
            if m[i]> n/2: return i
        return "NO"
    for x in a:
        try: m[x]+=1
        except: m[x]=1
    print(cnt(m))


