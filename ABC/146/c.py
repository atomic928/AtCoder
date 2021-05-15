a,b,x = map(int,input().split())
i = 1
kei = a+b
ans = False

while kei <= x:
  i += 1
  kei = a*(10**(i-1))+b*i
  ans = True

if ans:
  i -= 1

n = (x-b*i)//a

if n >= 10**i:
  n = 10**i - 1
if n < 1:
  print(0)
elif n <= 10**9:
  print(n)
else:
  print(10**9)
