from collections import Counter

n = int(input())
a = list(map(lambda x: int(x)%200, input().split()))
ad = Counter(a)

ans = 0

for i,v in ad.items():
  if v > 1:
    ans += (v*(v-1))//2

print(ans)