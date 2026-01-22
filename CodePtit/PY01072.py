from itertools import combinations as cb

n,k = map(int,input().split())

comb = cb(sorted(set(input().split()),key=int),k)
print('\n'.join([' '.join(x) for x in comb]))