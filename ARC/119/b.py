n = int(input())
s = list(input())
t = list(input())

s_zero, t_zero = [], []

ans = 0

for i in range(n):
  if s[i] == "0":
    s_zero.append(i)
  if t[i] == "0":
    t_zero.append(i)
  
if len(s_zero) != len(t_zero):
  print(-1)
else:
  for i in range(len(s_zero)):
    if s_zero[i] != t_zero[i]:
      ans += 1
  print(ans)