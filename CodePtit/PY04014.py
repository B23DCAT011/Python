


from functools import reduce
from decimal import ROUND_HALF_UP, Decimal
class stu:
    def __init__(self, i, n, a) -> None:
        self.code = f'HS{str(i).zfill(2)}'
        self.name = n
        self.tbc = (a[0]*2 + a[1]*2 + reduce(lambda x, y: x+y, a[2:]))/12
        self.tbc = (self.tbc).quantize(Decimal('0.1'), ROUND_HALF_UP)
        if self.tbc >= 9: self.type = 'XUAT SAC'
        elif self.tbc >= 8: self.type = 'GIOI'
        elif self.tbc >= 7: self.type = 'KHA'
        elif self.tbc >= 5: self.type = 'TB'
        else: self.type = "YEU"
a = []
for i in range(int(input())):
    a.append(stu(i + 1, input(), [Decimal(x) for x in input().split()]))
a.sort(key = lambda x: (-x.tbc, x.code))
for i in a: print(i.code, i.name, i.tbc, i.type)

# 3
# Luu Thuy Nhi
# 9.3  9.0  7.1  6.5  6.2  6.0  8.2  6.7  4.8  5.5
# Le Van Tam
# 8.0  8.0  5.5  9.0  6.8  9.0  7.2  8.3  7.2  6.8
# Nguyen Thai Binh
# 9.0  6.4  6.0  7.5  6.7  5.5  5.0  6.0  6.0  6.0