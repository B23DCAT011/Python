
a = {}

def minute(s : str):
    h,m = s.split(":")
    return int(h)*60 + int(m)

class tp:

    def __init__(self,n,start,end,m):
        self.name = n
        self.water = m
        self.time = minute(end)-minute(start)
t = 1
for i in range(int(input())):
    x = tp(input(),input(),input(),int(input()))
    if a.get(x.name) == None:
        x.code = 'T' + str(t).zfill(2)
        t+=1
        a[x.name] = x
    else:
        a[x.name].time += x.time
        a[x.name].water += x.water
for i in a:
    print(a[i].code,a[i].name,f'{a[i].water/(a[i].time/60):.2f}')

# 10
# Dong Anh
# 07:30
# 08:00
# 60
# Cau Giay
# 07:45
# 08:12
# 50
# Soc Son
# 08:00
# 09:15
# 78
# Dong Anh
# 18:50
# 20:00
# 88
# Cau Giay
# 19:01
# 20:00
# 77
# Soc Son
# 19:06
# 20:21
# 66
# Dong Anh
# 21:00
# 21:40
# 49
# Cau Giay
# 21:50
# 22:20
# 68
# Dong Anh
# 22:15
# 23:45
# 30
# Cau Giay
# 22:50
# 23:45
# 35