from fractions import Fraction

a,b,c,d = map(int,input().split())
sa = b-a
yozishou = b//c + b//d

if a%c == 0:
  yozishou -= a//c - 1
else:
  yozishou -= a//c

if a%d == 0:
  yozishou -= a//d - 1
else:
  yozishou -= a//d

bunsuu = Fraction(c,d)
kazu = list(map(int, str(bunsuu).split("/")))
if c == d:
  seki = c
else:
  seki = kazu[0]*kazu[1]*(c//kazu[0])
kaburi = b//seki

if a%seki == 0:
  kaburi -= a//seki-1
else:
  kaburi -= a//seki

print(sa+1-yozishou+kaburi)