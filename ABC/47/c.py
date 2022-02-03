import sys

#input()
def I(): return sys.stdin.readline().rstrip()
#list(input())
def SI(): return list(I())
#int(input())
def II(): return int(I())
#map(int,input().split())
def MI(): return map(int, I().split())
#map(str, input().split())
def MS(): return map(str, I().split())
#list(map(int,input().split()))
def LI(): return list(MI())
#行列
def LLI(rows_number): return [LI() for _ in range(rows_number)]
#文字の行列
def LSI(rows_number): return [SI() for _ in range(rows_number)]

s = SI()

ans = 0
 
for i in range(len(s)-1):
  if s[i+1] != s[i]:
    ans += 1
    
print(ans)