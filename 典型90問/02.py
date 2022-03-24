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
ls = []

# 奇数の場合は正しくない
if n%2 == 1:
  exit()

for i in range(2**n):
  s = ""
  left = 0
  right = 0
  for j in range(n):
    if i >> j & 1:
      left += 1
      s += "("
    else:
      right += 1
      s += ")"
    # 正しくなくなったらbreak
    if left < right:
      break
  else:
    # 左と右のカッコの数が等しいときだけ追加
    if left == right:
      ls.append(s)
    
# 辞書順に並べ、出力
ls.sort()
for i in ls:
  print(i)