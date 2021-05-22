n = int(input())
a,b,c = map(int,input().split())
ans = 10**4

for i in range(10000):
  for j in range(10000-i):
    if a*i+b*j > n: break
    k = n-(a*i+b*j)
    if k%c == 0:
      ans = min(ans, i+j+k//c)

print(ans)