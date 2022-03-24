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

n, l = MI()
k = II()
a = [0]+LI()

#それぞれの切れ端の長さを求める
lenls = [0]*(n+1)
a.append(l)
for i in range(n+1):
  lenls[i] = a[i+1]-a[i]

#二分探索で全ての切れ端がある長さ以上になるものを求める
Min = 1
Max = l
Mean = (Min+Max)//2

while Min != Mean:
  piece_number = 0
  piece_len = 0
  for i in range(n+1):
    piece_len += lenls[i]
    if piece_len >= Mean:
      piece_number += 1
      piece_len = 0
  if piece_number > k:
    Min = Mean
  else:
    Max = Mean
  Mean = (Min+Max)//2
  
print(Mean)
  
  
  