
class ThiSinh:

    def __init__(self,name,ns,x,y,z):
        self.name = name
        self.ns = ns
        self.total = x+y+z

    def printThiSinh(self):
        return self.name + " " + self.ns + " " + str(round(self.total,1))


if __name__ == "__main__":
    name = input()
    ns = input()
    x = float(input())
    y = float(input())
    z = float(input())

    thisinh = ThiSinh(name,ns,x,y,z)
    print(thisinh.printThiSinh())