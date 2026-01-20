

def sum_check(s):
    sum=0
    for i in s:
        sum+= int(i)
    return sum

for _ in range(int(input())):
    string = input()
    if str(sum_check(string)) == ''.join(reversed(str(sum_check(string)))):
        if sum_check(string)<10:
            print("NO")
        else:
            print("YES")
    else:
        print("NO")