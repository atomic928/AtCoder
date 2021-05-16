from collections import Counter
from itertools import combinations

s = list(input())
kazu = Counter(s)
maru = kazu['o']
batu = kazu['x']
hatena = kazu['?']

ans = 0

if maru >= 5 or batu == 10:
  print(0)
elif maru == 4:
  print(24)
elif maru == 3:
  ans += hatena*24
  ans += 36
  print(ans)
elif maru == 2:
  hatenacom = len(list(combinations([*range(hatena)], 4-maru)))
  ans += hatenacom*24
  ans += 12*hatena
  ans += 24*hatena
  ans += 14
  print(ans)
elif maru == 1:
  hatenacom = len(list(combinations([*range(hatena)], 4-maru)))
  ans += hatenacom*24
  ans += 4*hatena
  hatenacom = len(list(combinations([*range(hatena)], 2)))
  ans += 24*hatenacom
  ans += 12*hatenacom
  ans += 6*hatena
  ans += 4*hatena
  ans += 1
  print(ans)
else:
  print(hatena**4)

