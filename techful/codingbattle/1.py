n = int(input())
p = list(map(int,input().split()))
p.sort(reverse=True)
pl = []
for i in range(n):
  if i%2 == 0:
    pl.append(p[i//2])
  else:
    pl.append(sorted(p)[i//2])
ans = 10e10

if n < 10:
  for i in range(1, 2**n-1):
    X = 0
    count = 0
    amari = []
    for j in range(n):
      if ((i>>j)&1):
        X += p[j]
      else:
        count += 1
        amari.append(p[j])
    for k in range(1, 2**count):
      Y = 0
      for l in range(count):
        if ((k>>l)&1):
          Y += amari[l]
      ans = min(ans, abs(X-Y))
else:
  for i in range(1, 2**(n-2)):
    X = 0
    count = 0
    amari = []
    for j in range(n):
      if ((i>>j)&1):
        X += pl[j]
      else:
        count += 1
        amari.append(pl[j])
    for k in range(1, 2**count):
      Y = 0
      for l in range(count):
        if ((k>>l)&1):
          Y += amari[l]
      ans = min(ans, abs(X-Y))
      if ans == 0:
        exit(print(0))

print(ans)