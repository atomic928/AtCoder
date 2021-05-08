n = int(input())
s = list(input())
q = int(input())

hanntenn = 0

for i in range(q):
  t,a,b = map(int,input().split())
  if t == 1:
    if hanntenn%2 == 0:
      s[a-1], s[b-1] = s[b-1], s[a-1]
    else:
      if a-1 < n:
        if b-1 < n:
          s[a-1+n], s[b-1+n] = s[b-1+n], s[a-1+n]
        else:
          s[a-1+n], s[b-1-n] = s[b-1-n], s[a-1+n]
      else:
        if b-1 < n:
          s[a-1-n], s[b-1+n] = s[b-1+n], s[a-1-n]
        else:
          s[a-1-n], s[b-1-n] = s[b-1-n], s[a-1-n]
  else:
    hanntenn += 1
if hanntenn%2 == 0:
  print("".join(s))
else:
  s = s[n:] + s[:n]
  print("".join(s))