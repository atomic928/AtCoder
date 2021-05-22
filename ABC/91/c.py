from operator import countOf, itemgetter

n = int(input())
ab = [list(map(int,input().split())) for _ in range(n)]
cd = [list(map(int,input().split())) for _ in range(n)]

ab.sort(key = itemgetter(1))
ab.sort(key = itemgetter(0))
cd.sort(key = itemgetter(0))

ans = 0

for i in range(n):
  save = []
  for j in range(len(ab)):
    if ab[j][0] < cd[i][0]:
      save.append(ab[j])
    else:
      break
  save.sort(key=itemgetter(1), reverse=True)
  for k in save:
    if k[1] < cd[i][1]:
      ab.pop(ab.index(k))
      ans += 1
      break

print(ans)