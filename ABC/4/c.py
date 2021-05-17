n = int(input())
state = n//5%6

ans = []

for i in range(6):
  ans.append((state+1+i)%6)

for i in range(n%5):
  ans[i], ans[i+1] = ans[i+1], ans[i]

for i in ans:
  if i == 0:
    print(6, end="")
  else:
    print(i, end="")
