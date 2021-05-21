from itertools import accumulate

n = int(input())
c1 = [0]*n
c2 = [0]*n
pl = []

for i in range(n):
  c, p = map(int,input().split())
  if c == 1:
    c1[i] += p + c1[i-1]
    c2[i] += c2[i-1]
  else:
    c1[i] += c1[i-1]
    c2[i] += p + c2[i-1]
  pl.append(p)

q = int(input())

for i in range(q):
  l, r = map(int,input().split())
  ans1 = c1[r-1] - c1[l-1]
  ans2 = c2[r-1] - c2[l-1]
  if l-1 == 0:
    ans1 += c1[0]
    ans2 += c2[0]
  print(ans1, ans2)