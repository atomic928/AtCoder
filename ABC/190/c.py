n, m = map(int,input().split())
abl = [list(map(int,input().split())) for _ in range(m)]
k = int(input())
cd = [list(map(int,input().split())) for _ in range(k)]

ans = 0

for i in range(2**k):
  check = [False]*n
  count = 0
  for j in range(k):
    if int(format(i, '016b')[-1-j]):
      check[cd[j][1]-1] = True
    else:
      check[cd[j][0]-1] = True
  for ab in abl:
    if check[ab[0]-1] and check[ab[1]-1]:
      count += 1
  ans = max(ans, count)

print(ans)
