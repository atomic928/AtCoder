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

n, m = MI()
a = [SI() for _ in range(n)]
b = [SI() for _ in range(m)]

for i in range(n-m+1):
  for j in range(n-m+1):
    flag = 1
    for k in range(m):
      for l in range(m):
        if b[k][l] != a[i+k][j+l]:
          flag = 0
    if flag:
      sys.exit(print("Yes"))
print("No")
