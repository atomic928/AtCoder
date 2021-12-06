import sys
from typing import no_type_check

#input()
def I(): return sys.stdin.readline().rstrip()
#list(input())
def SI(): return list(sys.stdin.readline().rstrip())
#int(input())
def II(): return int(sys.stdin.readline().rstrip())
#map(int,input().split())
def MI(): return map(int, sys.stdin.readline().rstrip().split())
#map(str, input().split())
def MS(): return map(str, sys.stdin.readline().rstrip().split())
#list(map(int,input().split()))
def LI(): return list(map(int, sys.stdin.readline().rstrip().split()))
#行列
def LLI(rows_number): return [LI() for _ in range(rows_number)]
#文字の行列
def LSI(rows_number): return [SI() for _ in range(rows_number)]

from itertools import accumulate

s = I()
n = len(s)
cl = [0]*n
hl = [0]*n
ol = [0]*n
kl = [0]*n
ul = [0]*n
dl = [0]*n
al = [0]*n
il = [0]*n

for i in range(n):
  if s[i] == "c":
    cl[i] += 1
  if s[i] == "h":
    hl[i] = 1
  if s[i] == "o":
    ol[i]= 1
  if s[i] == "k":
    kl[i]+= 1
  if s[i] == "u":
    ul[i] += 1
  if s[i] == "d":
    dl[i] += 1
  if s[i] == "a":
    al[i] += 1
  if s[i] == "i":
    il[i] += 1

cl = list(accumulate(cl))
  
ch = [0]*n
cho = [0]*n
chok = [0]*n
choku = [0]*n
chokud = [0]*n
chokuda = [0]*n
chokudai = [0]*n

for i in range(n):
  if hl[i]:
    ch[i] = cl[i]

ch = list(accumulate(ch))

for i in range(n):
  if ol[i]:
    cho[i] = ch[i]

cho = list(accumulate(cho))

for i in range(n):
  if kl[i]:
    chok[i] = cho[i]

chok = list(accumulate(chok))

for i in range(n):
  if ul[i]:
    choku[i] = chok[i]

choku = list(accumulate(choku))

for i in range(n):
  if dl[i]:
    chokud[i] = choku[i]

chokud = list(accumulate(chokud))

for i in range(n):
  if al[i]:
    chokuda[i] = chokud[i]

chokuda = list(accumulate(chokuda))

for i in range(n):
  if il[i]:
    chokudai[i] = chokuda[i]

chokudai = list(accumulate(chokudai))

print(chokudai[n-1])