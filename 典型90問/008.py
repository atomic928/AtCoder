from bisect import bisect_left

n = int(input())
s = input()
a = []
t = []
c = []
o = []
d = []
e = []
r = []

for i in range(n):
  if s[i] == "a":
    a.append(i)
  elif s[i] == "t":
    t.append(i)
  elif s[i] == "c":
    c.append(i)
  elif s[i] == "o":
    o.append(i)
  elif s[i] == "d":
    d.append(i)
  elif s[i] == "e":
    e.append(i)
  elif s[i] == "r":
    r.append(i)

ans = 0

for i1 in a:
  kosuu = 1
  kosuu *= bisect_left(t, i1)
  for i2 in t[bisect_left(t, i1):]:
    
      for i3 in c:
        if i3 > i2:
          for i4 in o:
            if i4 > i3:
              for i5 in d:
                if i5 > i4:
                  for i6 in e:
                    if i6 > i5:
                      for i7 in r:
                        if i7 > i6:
                          ans += 1 


print(ans)