from operator import itemgetter
from copy import deepcopy

k, n, m = map(int,input().split())
a = list(map(int,input().split()))

bsum = 0
b = []

for i in a:
  b.append([i*m//n, abs((i*m//n)/m - i/n)])
  bsum += i*m//n

roop = m - bsum

for i in range(roop):
  sorted(b, key = itemgetter(1), reverse=True)[i][0] += 1

for i in range(k):
  print(b[i][0], end = " ")