n = int(input())
a = list(map(int,input().split()))
ans = a[0]**2*(n-1)
pre = a[0]

for i in range(1, n):
  ans += a[i]**2*(n-1)
  ans -= 2*a[i]*pre
  pre += a[i]

print(ans)