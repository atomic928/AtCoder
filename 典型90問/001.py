n, l = map(int,input().split())
k = int(input())
a = list(map(int,input().split()))
sa = [0]*(n+1)
sa[0] = a[0]

a.append(l)

for i in range(1,n+1):
  sa[i] = a[i] - a[i-1]

piecels = 1
piecelb = 10**9
piecel = (piecels+piecelb)//2

while piecels != piecel:
  kosuu = 0
  leng = 0
  for i in sa:
    leng += i
    if leng >= piecel:
      leng = 0
      kosuu += 1
  if kosuu > k:
    piecels = piecel
  else:
    piecelb = piecel
  piecel = (piecels+piecelb)//2

print(piecel)