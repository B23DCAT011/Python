
string = input()

cnt1 = 0
cnt2 = 0

for item in string:
    if(item.isupper()):
        cnt1+=1
    else:
        cnt2+=1

if cnt1 > cnt2:
    print(string.upper())
else:
    print(string.lower())


