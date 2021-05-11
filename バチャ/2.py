q = int(input())

for i in range(q):
  hidari = 0
  migi = 0
  shuusei = 0
  s = input()
  ss = ""
  for c in s:
    if c == "(":
      hidari += 1
      ss += "("
    else:
      migi += 1
      ss += ")"
    
    if migi > hidari:
      shuusei += 1
      hidari += 1
      migi -= 1
      ss = ss[:migi+hidari-1] + "("
  shuusei += hidari - migi - shuusei
  if (len(s)/2-shuusei)%4 == 0:
    print("Yes")
  elif "()()" in ss and (len(s)/2 - shuusei)%4 == 2:
    print("Yes")
  else:
    print("No")