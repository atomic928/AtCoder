from collections import Counter

n = int(input())
a = list(map(int,input().split()))
b = list(map(int,input().split()))
c = list(map(int,input().split()))

bc = []

for i in range(n):
  bc.append(b[c[i]-1])

bccount = Counter(bc)

ans = 0

for i in range(n):
  ans += bccount[a[i]]

print(ans)