from math import factorial

a,b,k = map(int,input().split())
zen = factorial(a+b)//(factorial(a)*factorial(b))
count = 0
n = 0
ans = ""

for i in range(a+b):
  if a == 0:
    ans += "b"
    continue
  if b == 0:
    ans += "a"
    continue
  n = factorial(a+b-1)//(factorial(a-1)*factorial(b))
  if count+n < k:
    ans += "b"
    b -= 1
    count += n
  else:
    ans += "a"
    a -= 1

print(ans)