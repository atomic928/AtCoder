from itertools import combinations


n, k = map(int,input().split())
count = 0
ten = 0
jun = 0
while count < k:
  i = 0
  jun = k-count
  count += len(list(combinations([x for x in range(n)], i)))
  ten = i+3
  i += 1
