for t in range(int(input())):
    def ans(a):
        for i in a:
            if i!= '1' and i!='0' and i!='2': return "NO"
        return "YES"
    print(ans(input()))