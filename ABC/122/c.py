n, q = map(int,input().split())
s = input()
ac = [0]*n
count = 0

for i in range(n-1):
  if s[i] == "A" and s[i+1] == "C":
    count += 1
  ac[i+1] = count

for i in range(q):
  l, r = map(int,input().split())
  ans = ac[r-1]-ac[l-1]
  print(ans)