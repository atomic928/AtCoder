from collections import Counter
s = input()
count = Counter(s)
zero = count['0']
one = count['1']

ans = 2*min(zero, one)

print(ans)