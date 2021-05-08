n = input()
ln = len(n)
ans = 0
if ln%2 == 0 and ln > 2:
  for i in range(ln//2-1):
    ans += 10**i*9
elif ln%2 == 1 and ln > 1:
  for i in range((ln+1)//2-1):
    ans += 10**i*9

if ln%2 == 0:
  if int(n[:ln//2]) <= int(n[ln//2:]):
    ans += int(n[:ln//2])-ans
  else:
    ans += int(n[:ln//2])-1-ans

print(ans)
