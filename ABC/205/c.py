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

a,b,c = MI()
if a >= 0 and b >= 0:
  if a < b:
    print("<")
  elif a > b:
    print(">")
  else:
    print("=")
elif a < 0 and b >= 0:
  if c%2 == 0:
    if -a < b:
      print("<")
    elif -a > b:
      print(">")
    else:
      print("=")
  else:
    print("<")
elif a >= 0 and b < 0:
  if c%2 == 0:
    if a < -b:
      print("<")
    elif a > -b:
      print(">")
    else:
      print("=")
  else:
    print(">")
else:
  if c%2 == 0:
    if -a < -b:
      print("<")
    elif -a > -b:
      print(">")
    else:
      print("=")
  else:
    if a < b:
      print("<")
    elif a > b:
      print(">")
    else:
      print("=")