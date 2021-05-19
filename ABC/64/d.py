n = int(input())
s = list(input())

left = 0
right = 0

lplus = 0

for i in s:
  if i == "(":
    left += 1
  else:
    right += 1
  
  if right > left:
    lplus += 1
    left += 1

rplus = left - right

for _ in range(lplus):
  print("(", end="")

for i in s:
  print(i, end="")

for _ in range(rplus):
  print(")", end="")