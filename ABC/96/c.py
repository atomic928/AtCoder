h, w = map(int,input().split())
s = [list(input()) for _ in range(h)]

check = [[False]*w for _ in range(h)]

for i in range(h):
  for j in range(w):
    if j != w-1 and i != h-1:
      if s[i][j] == "#":
        if s[i][j+1] == "#":
          check[i][j] = True
          check[i][j+1] = True
        if s[i+1][j] == "#":
          check[i][j] = True
          check[i+1][j] = True
      else:
        check[i][j] = True
    elif j != w-1:
      if s[i][j] == "#":
        if s[i][j+1] == "#":
          check[i][j] = True
          check[i][j+1] = True
      else:
        check[i][j] = True
    elif i != h-1:
      if s[i][j] == "#":
        if s[i+1][j] == "#":
          check[i][j] = True
          check[i+1][j] = True
      else:
        check[i][j] = True
    else:
      if s[i][j] == ".":
        check[i][j] = True

for i in range(h):
  if sum(check[i]) != w:
    exit(print("No"))

print("Yes")
