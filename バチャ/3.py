import sys

#input()
def I(): return sys.stdin.readline().rstrip()
#list(input())
def SI(): return list(sys.stdin.readline().rstrip())
#int(input())
def II(): return int(sys.stdin.readline().rstrip())
#map(int,input().split())
def MI(): return map(int, sys.stdin.readline().rstrip().split())
#map(str, input().split())
def MS(): return map(str, sys.stdin.readline().rstrip().split())
#list(map(int,input().split()))
def LI(): return list(map(int, sys.stdin.readline().rstrip().split()))
#行列
def LLI(rows_number): return [LI() for _ in range(rows_number)]

h, w = MI()
s = [SI() for _ in range(h)]
 
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