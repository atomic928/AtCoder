n = int(input())
xyh = [list(map(int,input().split())) for _ in range(n)]
sum_xyh = []
mxh = 0

for i in range(n):
  sum_xyh.append(xyh[i][0]+xyh[i][1]+xyh[i][2])
  mxh = max(mxh, xyh[i][2])

sum_xyh = list(set(sum_xyh))

sum_ans = sum(sum_xyh)//len(sum_xyh)
x = 1
flag = True
while flag:
  y = sum_ans - mxh - x
  for i in range(n):
    if xyh[i][2] != mxh - abs(xyh[i][0]-x) -abs(xyh[i][1]-y):
      x += 1
      break
  else:
    flag = False
  if abs(x-y) <= 1:
    mxh += 1
    x = 1

print(x, y, mxh)