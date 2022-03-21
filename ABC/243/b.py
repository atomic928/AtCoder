from collections import defaultdict
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
a = LI()
b = LI()


half_match = 0
perfect_match = 0

for i in range(n):
  if a[i] == b[i]: 
    perfect_match += 1
  if a[i] in set(b): 
    half_match += 1
  

print(perfect_match)
print(half_match-perfect_match)