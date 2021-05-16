from bisect import bisect_left

n = int(input())
s = input()
a = 0
t = 0
c = 0
o = 0
d = 0
e = 0
r = 0

for i in range(n):
  if s[i] == "a":
    a += 1
  elif s[i] == "t":
    t += a
  elif s[i] == "c":
    c += t
  elif s[i] == "o":
    o += c
  elif s[i] == "d":
    d += o
  elif s[i] == "e":
    e += d
  elif s[i] == "r":
    r += e

print(r%(10**9+7))

