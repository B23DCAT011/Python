import math

n,x = input().split()
f=[1 for x in range(10002)]
f[0],f[1] = 0,0
nt=[]
for i in range(2,10000):
    if f[i]==1:
       nt.append(i)
       for j in range(i*i,10002,i):
           f[j]=0
pre = int(x)
print(x,end=' ')
for i in range(int(n)):
    print(pre+nt[i],end=' ')
    pre+=nt[i]