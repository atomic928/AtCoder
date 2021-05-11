from operator import itemgetter
from copy import deepcopy

k, n, m = map(int,input().split())
a = list(map(int,input().split()))

bsum = 0
b = []

for i in a:
  b.append([i*m//n, abs((i*m//n)/m - i/n)])
  bsum += i*m//n
print(b)

# bsave = deepcopy(b)
# b.sort(key = itemgetter(1), reverse=True)

roop = m - bsum

for _ in range(roop):
  mindex = b.index(max(b, key=itemgetter(1)))
  b[mindex][0] += 1
  b[mindex][1] = abs((b[mindex][0]*m//n)/m - a[mindex]/n)
print(b)