import math


r, x, y = map(int,input().split())
kyori = math.sqrt(x**2+y**2)
if r <= kyori:
  ans = math.ceil(kyori/r)
else:
  ans = 2
print(ans)