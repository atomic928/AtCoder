import math

a,b,w = map(int,input().split())
n = math.floor(1000*w/a)
if 1000*w <= b*n:
  print(math.ceil(1000*w/b), n)
else:
  print("UNSATISFIABLE") 