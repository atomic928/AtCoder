n = int(input())
mx = 0
INDEX = 0

for i in range(2,n+1):
  print("?", 1, i)
  dist = int(input())
  if mx < dist:
    mx = dist
    INDEX = i

for i in range(1, n+1):
  if i == INDEX: continue
  print("?", INDEX, i)
  dist = int(input())
  mx = max(mx, dist)

print("!", mx)