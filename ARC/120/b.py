import sys

#input()
def I(): return sys.stdin.readline().rstrip()
#int(input())
def II(): return int(sys.stdin.readline().rstrip())
#map(int,input().split())
def MI(): return map(int, sys.stdin.readline().rstrip().split())
#list(map(int,input().split()))
def LI(): return list(map(int, sys.stdin.readline().rstrip().split()))
#行列
def LLI(rows_number): return [LI() for _ in range(rows_number)]

h,w = MI()
s = [list(I()) for _ in range(h)]
ans = 1


if s[0][0] == ".":
  ans *= 2
if s[h-1][w-1] == ".":
  ans *= 2

for i in range(1, h):
  check = ""
  for j in range(i+1):
    if j > w-1:
      break
    if s[i-j][j] == "R":
      if check == "B":
        print(0)
        exit()
      else:
        check = "R"
    elif s[i-j][j] == "B":
      if check == "R":
        print(0)
        exit()
      else:
        check = "B"
  if check == "":
    ans *= 2
  
for i in range(1, w-1):
  check = ""
  for j in range(i+1):
    if j > h-1:
      break
    if s[h-1-j][w-1-i+j] == "R":
      if check == "B":
        print(0)
        exit()
      else:
        check = "R"
    elif s[h-1-j][w-1-i+j] == "B":
      if check == "R":
        print(0)
        exit()
      else:
        check = "B"
  if check == "":
    ans *= 2

print(ans%998244353)