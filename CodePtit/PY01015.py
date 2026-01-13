def check(s):
    for i in range(1,len(s)):
        if(s[i]<s[i-1]):
            return False
    return True


t = int(input())

for _ in range(t):
    string = list(input())
    if(check(string)):
        print("YES")
    else:
        print("NO")