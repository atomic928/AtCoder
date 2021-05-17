n, k = map(int,input().split())
for i in range(k):
  nl = list(str(n))
  g1 = int("".join(sorted(nl, reverse=True)))
  g2 = int("".join(sorted(nl)))
  n = g1-g2

print(n)