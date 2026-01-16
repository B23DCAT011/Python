import math



t = int(input())
for i in range(t):
    n = input()
    n_reversed = ''.join(reversed(n))

    print("YES") if math.gcd(int(n),int(n_reversed))==1 else print("NO")