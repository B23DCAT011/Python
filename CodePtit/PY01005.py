



string = list(input())
cnt=0
for i in range(len(string)):
    if(string[i]== "4" or string[i]=="7"):
        cnt+=1

if(cnt == 4 or cnt ==7):
    print("YES")
else:
    print("NO")
