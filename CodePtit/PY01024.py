


def TongChiaHetCho10(s):
    cnt = 0
    for item in s:
        cnt += int(item)
    return cnt%10 == 0
def Cach2DonVi(s):
    for i in range(1,len(s)):
        if(abs(int(s[i])-int(s[i-1]))!=2):
            return False
    return True

for _ in range(int(input())):
    s = input()
    if(TongChiaHetCho10(s) and Cach2DonVi(s)):
        print("YES")
    else:
        print("NO")