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

n = II()
s = SI()
ans = (n*(n-1))//2



pre = s[0]
count = 1
for i in range(1, n):
  if pre == s[i]: 
    count += 1
    if i == n-1:
      ans -= (count*(count-1))//2
  else:
    pre = s[i]
    ans -= (count*(count-1))//2
    count = 1

print(ans)