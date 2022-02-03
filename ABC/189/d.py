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

n = II()

#y_nがTrueの数
ans = 1

for i in range(n):
  s = I()
  if s == "OR":
    #y_nがFlaseの場合でも、x_nがTrueなら良いので、その分の数を足す
    ans += 2**(i+1)
    
print(ans)

