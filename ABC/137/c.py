from collections import Counter
from operator import itemgetter

n = int(input())

save = []

for i in range(n):
  s = list(input())
  s.sort()
  save.append("".join(s))

count = Counter(save)

ans = 0

for i, v in count.items():
  if v == 1:
    continue
  else:
    ans += v*(v-1)//2

print(ans)