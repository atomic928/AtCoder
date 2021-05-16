h, w = map(int,input().split())
a = [list(input()) for _ in range(h)]
score = [0]*2

print(a)

for i in range(h):
  for j in range(w):
    if i == 0 and j == 0:
      a[i][j][0] = 0
    else:
      if a[i][j][0] == "+":
        a[i][j][0] = 1
      else:
        a[i][j][0] = -1

for i in range(h):
  for j in range(w):
    if i != h-1 and j != w-1:
      a[i][j][1] += a[i+1][j][0] + a[i][j+1][0]
    elif i == h-1 and j == w-1:
      pass
    elif i == h-1:
      a[i][j][1] += a[i][j+1][0]
    else:
      a[i][j][1] += a[i+1][j][0]


nh = 0
nw = 0
for i in range(h+w-2):
  if nh != h-1 and nw != w-1:
    if a[nh+1][nw][1] < a[nh][nw+1][1]:
      nh += 1
      score[i%2] += a[nh][nw][0] 
    else:
      nw += 1
      score[i%2] += a[nh][nw][0]
  elif nh == h-1 and nw == w-1:
    pass
  elif nh == h-1:
    nw += 1
    score[i%2] += a[nh][nw][0]
  else:
    nh += 1
    score[i%2] += a[nh][nw][0]

if score[0] < score[1]:
  print("Aoki")
elif score[0] > score[1]:
  print("Takahashi")
else:
  print("Draw")