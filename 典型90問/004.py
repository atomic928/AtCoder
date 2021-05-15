h, w = map(int,input().split())
tate = [0]*w
yoko = []
al = []

for i in range(h):
  a = list(map(int,input().split()))
  al.append(a)
  yoko.append(sum(a))
  for j in range(w):
    tate[j] += a[j]
  
for i in range(h):
  for j in range(w):
    print(yoko[i] + tate[j] - al[i][j], end = " ")
  print("")