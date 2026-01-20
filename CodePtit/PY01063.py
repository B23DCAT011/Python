t = int(input())
for _ in range(t):
    s1 = input()
    s2 = input()
    n = len(s2)
    cnt = 0

    i = 0
    while i <= len(s1) - n:
        if s1[i:i+n] == s2:
            cnt += 1
            i += n
        else:
            i += 1
    print(cnt)

