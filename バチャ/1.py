from math import sqrt

n, m = map(int,input().split())
xyr = [list(map(int,input().split())) for _ in range(n)]
xy = [list(map(int,input().split())) for _ in range(m)]
mndist = [10e10]
mmdist = [10e10]
nr = [10e10]
if n > 0:
  for i in range(n):
    nr.append(xyr[i][2])
    if m > 0:
      for j in range(m):
        mndist.append(sqrt((xyr[i][0]-xy[j][0])**2+(xyr[i][1]-xy[j][1])**2)-xyr[i][2])

if m > 1:
  for i in range(m):
    for j in range(i+1, m):
      mmdist.append(sqrt((xy[i][0]-xy[j][0])**2+(xy[i][1]-xy[j][1])**2))


print(min(min(nr), min(mndist), min(mmdist)/2))