for t in range(int(input())):
    def ans(a):
        if(len(a)<3) : return "NO"
        i=0
        while i<len(a)-1 and a[i]<a[i+1]: i+=1
        while i<len(a)-1 and a[i]>a[i+1]: i+=1
        if i == len(a)-1: return "YES"
        return "NO"
    print(ans(input()))