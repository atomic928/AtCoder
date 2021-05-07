n = int(input())
a = list(map(int,input().split()))
b = list(map(int,input().split()))
mi = 1001
mx = 0

mi = min(mi, max(a))
mx = max(mx, min(b))

if mi <= mx:
  print(mx-mi+1)
else:
  print(0)