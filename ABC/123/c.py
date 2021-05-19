from math import ceil

n = int(input())
norimono = [int(input()) for _ in range(5)]
mi_n = min(norimono)
ans = 4+ceil(n/mi_n)

print(ans)