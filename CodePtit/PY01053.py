import math


def sum_check(s):
    sums=0
    for i in s:
        sums+= int(i)
    return sums



for _ in range(int(input())):
    string = input()
    sums = sum_check(string)
    if sums%3==0:
        print("YES")
    else:
        print("NO")
