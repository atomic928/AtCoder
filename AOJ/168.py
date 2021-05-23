from math import ceil
from sys import stdin

dp = [0]*40
dp[0], dp[1], dp[2] = 1, 2, 4

for i in range(3, 30):
  dp[i] += dp[i-1]+dp[i-2]+dp[i-3]

n = stdin.readline().rstrip()

while n != "0":
  print(ceil(dp[int(n)-1]/3650))
  n = stdin.readline().rstrip()