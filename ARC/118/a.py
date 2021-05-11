from math import ceil

t, N = map(int,input().split())

bairitu = 100

if (100+t)%4 == 0:
  bairitu //= 4
elif (100+t)%2 == 0:
  bairitu //= 2

if (100+t)%25 == 0:
  bairitu //= 25
elif (100+t)%5 == 0:
  bairitu //= 5

print((100+t)*ceil((100/t)*N)//100-1)
