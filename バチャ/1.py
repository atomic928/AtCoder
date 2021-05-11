from math import sqrt

n, m = map(int,input().split())
xyr = [list(map(int,input().split())) for _ in range(n)]
xy = [list(map(int,input().split())) for _ in range(m)]
mndist = []
mmdist = []
nr = []
for i in range(n):
  nr.append(xyr[i][2])
  for j in range(m):
    mndist.append(sqrt((xyr[i][0]-xy[j][0])**2+(xyr[i][1]-xy[j][1])**2)-xyr[i][2])

if m > 1:
  for i in range(m):
    for j in range(i+1, m):
      mmdist.append(sqrt((xy[i][0]-xy[j][0])**2+(xy[i][1]-xy[j][1])**2))



if mndist != [] and mmdist != [] and nr != []:
  print(min(min(mndist), min(mmdist)/2), min(nr))
elif mndist != [] and mmdist == []:
  print(min(min(mndist), min(nr)))
elif mmdist != [] and n == 0:
  print(min(mmdist)/2)
elif n > 0 and m == 0:
  print(min(nr))
