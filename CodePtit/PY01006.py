


t = int(input())

for j in range(t):
    string = list(input())
    cnt = 0
    for i in range(len(string)):
        if (string[i] == "4" or string[i] == "7"):
            cnt += 1

    if (cnt == len(string)):
        print("YES")
    else:
        print("NO")




