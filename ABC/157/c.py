n, m = map(int,input().split())
ans = ["a"]*n

for i in range(m):
  s,c = map(int,input().split())
  if s == 1 and c == 0 and n != 1:
    exit(print(-1))
  elif ans[s-1] == "a":
    ans[s-1] = str(c)
  elif ans[s-1] == str(c):
    pass
  else:
    exit(print(-1))
if n > 1:
  print(1 if ans[0] == "a" else ans[0], end="")
else:
  print(0 if ans[0] == "a" else ans[0], end="")

for i in range(1, n):
  print(0 if ans[i] == "a" else ans[i], end="")