t = int(input())

for _ in range(t):
    string = list(input())
    for i in range(0,len(string),2):
        print(string[i]*int(string[i+1]),end="")
    print()