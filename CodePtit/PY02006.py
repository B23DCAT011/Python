
def check(a,b):
    for i in range(len(a)):
        if a[i] > b[i] : return "NO"
    return  "YES"

for _ in range(int(input())):
    n = input()
    a,b = [int(x) for x in input().split()],[int(x) for x in input().split()]
    print(check(sorted(a),sorted(b)))cd
