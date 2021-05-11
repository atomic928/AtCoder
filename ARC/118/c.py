from itertools import combinations
import math

n = int(input())

sosuu = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97, 101, 103, 107, 109, 113, 127, 131, 137, 139, 149, 151, 157, 163, 167, 173, 179, 181, 191, 193, 197, 199, 211, 223, 227, 229, 233, 239]
retu = []

for conb in combinations(sosuu[:5+int(n/2500*53)], 3):
  tanni = 1
  ts = 0
  for c in list(conb):
    tanni *= c
  ts = tanni
  for i in range(3):
    while tanni <= 10000:
      retu.append(tanni)
      tanni *= list(conb)[i]
    tanni = ts


retu = sorted(set(retu), key = retu.index)

ans = [str(c) for c in retu[:n-1]] + [str(retu[-1])]
print(" ".join(ans))
