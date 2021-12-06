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
#文字の行列
def LSI(rows_number): return [SI() for _ in range(rows_number)]

S = I()

while S != "":
  if S[-5:] == "dream":
    S = S[:-5]
  elif S[-5:] == "erase":
    S = S[:-5]
  elif S[-7:] == "dreamer":
    S = S[:-7]
  elif S[-6:] == "eraser":
    S = S[:-6]
  else:
    break

if S == "":
  print("YES")
else:
  print("NO")