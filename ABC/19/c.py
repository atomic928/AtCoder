#bit使って0.5倍していく
n = int(input())
a = list(map(int,input().split()))
a = list(set(a))
n = len(a)

for i in range(n):
  for j in range(1, 30):
    a.append(a[i]*2**j)

ans = n - (30*n - len(list(set(a))))

print(ans)