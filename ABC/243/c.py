from operator import itemgetter
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
xy = LLI(n)
s = SI()

for i in range(n):
  isR = 0 if s[i] == "R" else 1
  xy[i].append(isR)

xy.sort(key=itemgetter(0))
xy.sort(key=itemgetter(1))

same_list = []

count = 1
for i in range(n-1):
  if xy[i][1] == xy[i+1][1]:
    count += 1
  else: 
    same_list.append(count)
    count = 1
else:
  same_list.append(count)
  

count = 0
for i in same_list:
  isR = 0
  for j in range(i):
    if xy[count][2] == 0: isR=1
    if isR and xy[count][2]: sys.exit(print("Yes"))
    count += 1
    
    
print("No")