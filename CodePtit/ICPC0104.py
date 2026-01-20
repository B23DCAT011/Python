import re


for i in range(int(input())):
    arr = sorted([int(x) for x in re.split("[a-z]+",input()) if x != ''])
    if len(arr)>0: print(arr[0])


