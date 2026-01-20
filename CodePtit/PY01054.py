import math


def mul_check(s):
    muls=1
    for i in s:
        if(int(i)==0):
            continue
        muls*= int(i)
    return muls



for _ in range(int(input())):
    string = input()
    print(mul_check(string))

