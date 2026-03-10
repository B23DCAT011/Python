

class HoaDon:

    def __init__(self,i,name,st,en):
        self.code = f'KH{str(i).zfill(2)}'
        self.name = name
        m = en-st
        if m > 100:
            self.giatien = ((m - 100) * 200 + 50 * (100 + 150)) * 1.05
        elif m > 50:
            self.giatien = ((m - 50) * 150 + 50 * 100) * 1.03
        else:
            self.giatien = m * 100 * 1.02

a = []
for i in range(int(input())):
    kh = HoaDon(i+1,input(),int(input()),int(input()))
    a.append(kh)
a.sort(key = lambda x: (-x.giatien,x.code) )
for kh in a: print(kh.code,kh.name,f'{kh.giatien:.0f}')


# 3
# Le Thi Thanh
# 468
# 500
# Le Duc Cong
# 160
# 230
# Ha Hue Anh
# 410
# 612