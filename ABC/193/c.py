n = int(input())

check = []

a, b = 2, 2

while a**b <= n:
  while a**b <= n:
    check.append(a**b)
    b += 1
  b = 2
  a += 1

print(n - len(set(check)))