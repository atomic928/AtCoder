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

N, K = MI()
INDEX = K**2//2
# A = LLI(n)
ans = 10**9+1
ls = [[] for _ in range((N-K+1)**2)]

if N == K:
  for i in range(N):
    a = LI()
    ls[0] += a
  ls.sort(reverse=True)
  sys.exit(print(ls[0][INDEX]))

for i in range(N):
  a = LI()
  if i == 0:
    for j in range(N-K+1):
      ls[i*2+j] += a[j:j+K]
  elif i == N-1:
    for j in range(N-K+1):
      ls[(i-1)*2+j] += a[j:j+K]
  else:
    for j in range(N-K+1):
      ls[i*2+j] += a[j:j+K]
      ls[(i-1)*2+j] += a[j:j+K]

for i in ls:
  i.sort(reverse=True)
  ans = min(ans, i[INDEX])

print(ans)
