

for _ in range(int(input())):
    s = input()
    s_re = ''.join(reversed(s))
    ok=1;
    for i in range(1,len(s)):
        if abs(ord(s[i])- ord(s[i-1])) == abs(ord(s_re[i])- ord(s_re[i-1])):
            continue;
        else:
            print("NO");
            ok=0;
            break;
    if ok==1:
        print("YES")