n = int(input())
hs = [list(map(int,input().split())) for _ in range(n)]

mi = 0
mx = n*10**9+1
ans = (mi+mx)//2

while mi != ans:
  check = 0
  deadtime = [int((ans-hs[i][0])/hs[i][1]) for i in range(n)]
  deadtime.sort()
  for i in range(n):
    if check <= deadtime[i]:
      check += 1
    else:
      mi = ans
      break
  else:
    mx = ans
  ans = (mi+mx)//2

print(ans+1)