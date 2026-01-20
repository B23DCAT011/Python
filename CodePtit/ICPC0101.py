
n = input()
a = map(int,input().split())
st = []

for i in a:
    if len(st) == 0 or (st[-1]+i)%2 == 1: st.append(i)
    else: st.pop(-1)
print(len(st))