n = int(input())
tpre, xpre, ypre = 0, 0, 0

for i in range(n):
  t, x, y = map(int,input().split())
  dis = abs(x - xpre) + abs(y - ypre)
  time = t - tpre
  if dis > time:
    exit(print("No"))
  else:
    if dis != time:
      if (time-dis)%2 == 1:
        exit(print("No"))
  tpre, xpre, ypre = t,x,y

print("Yes")
      