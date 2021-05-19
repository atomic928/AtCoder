n = int(input())
a = list(map(int,input().split()))

ans = float("inf")

for i in range(2**(n-1)):
  XOR = 0
  OR = 0
  for j in range(n):
    OR = OR|a[j]
    if ((i>>j)&1):
      XOR = XOR^OR
      OR = 0
  else:
    XOR = XOR^OR
  ans = min(ans, XOR)

print(ans)



  
