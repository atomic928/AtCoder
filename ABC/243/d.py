from multiprocessing.connection import answer_challenge
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

n, x = MI()
s = SI()

isE = x%2
if not isE: isE = 2
ans = isE

tbcount = 0

for i in range(n):
  if s[i] == "U":
    tbcount -= 1
    ans //= 2
  elif s[i] == "L":
    tbcount += 1
    ans *= 2
  else:
    tbcount += 1
    ans = ans*2+1

if x-isE != 0:    
  ans += (x-isE)*2**tbcount

print(ans)