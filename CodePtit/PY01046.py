

def move(st,m,en,n):
    if(n==0) : return
    move(st,en,m,n-1)
    print(f'{st} -> {en}')
    move(m,st,en,n-1)

move('A','B','C',int(input()))