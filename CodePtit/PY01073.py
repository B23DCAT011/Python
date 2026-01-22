from itertools import permutations as per

print('\n'.join([''.join(x) for x in per(input())]))