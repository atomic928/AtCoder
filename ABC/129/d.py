h, w = map(int,input().split())
s = [list(input()) for _ in range(h)]

check = [[0]*w for _ in range(h)]

for i in range(h):
  for j in range(w):
    if s[i][j] == "#":
      break
    
