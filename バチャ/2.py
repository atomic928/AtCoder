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

s = I()

if s == "WBWBWWBWBWBWWBWBWWBW":
  print("Do")
elif s == "WBWWBWBWBWWBWBWWBWBW":
  print("Re")
elif s == "WWBWBWBWWBWBWWBWBWBW":
  print("Mi")
elif s == "WBWBWBWWBWBWWBWBWBWW":
  print("Fa")
elif s == "WBWBWWBWBWWBWBWBWWBW":
  print("So")
elif s == "WBWWBWBWWBWBWBWWBWBW":
  print("La")
else:
  print("Si")