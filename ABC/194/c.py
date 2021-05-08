n = int(input())
a = list(map(int,input().split()))
ans = 0

for i in range(2, n+1):
  for j in range(1, i):
    ans += (a[i-1]-a[j-1])**2

print(ans)