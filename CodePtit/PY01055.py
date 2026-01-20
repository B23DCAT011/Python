

def check(s):
    if len(s)%2==0:
        return  False
    if s[0]==s[1]:
        return  False
    for i in range(0,len(s)-1-2,2):
        if s[i]!=s[i+2]:
            return False
    return True

for _ in range(int(input())):
    string = input()
    if check(string):
        print("YES")
    else:
        print("NO")

