t = int(input())

for i in range(t):
    string = list(input())
    x = len(string)
    if(string[0]==string[x-2] and string[1]==string[x-1]):
        print("YES")
    else:
        print("NO")
