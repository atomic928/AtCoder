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

N,K = MI()
ans = 0

if K == 2:
  ans += N
  if N == 3:
    ans += 6
  elif N%2 == 0 and N >= 4:
    ans += (((N//2)*(N//2-1))//2)*12
  elif N%2 == 1 and N >= 4:
    ans += (((N//2)*(N//2-1))//2)*6
    ans += ((((N+1)//2)*((N+1)//2-1))//2)*6
  if N == 5:
    ans += 6
  elif N%2 == 0 and N >= 6:
    ans += (((N//2)*(N//2-1)*(N//2-2))//6)*12
  elif N%2 == 1 and N >= 6:
    ans += (((N//2)*(N//2-1)*(N//2-2))//6)*6
    ans += ((((N+1)//2)*((N+1)//2-1)*((N+1)//2-2))//6)*6
elif K%2 == 0:
  ans += ((N+K//2)//K)**3
  ans += (N//K)**3
else:
  ans += (N//K)**3

print(ans)