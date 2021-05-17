n = int(input())
ans = 10**18+1

b = 0
a, c = divmod(n, 2**b)
ans2 = a+b+c

ans3 = 10**18+1


for _ in range(60):
  ans = ans2
  ans3 = min(ans3, ans)
  b += 1
  a, c = divmod(n, 2**b)
  ans2 = a+b+c

print(ans3)

