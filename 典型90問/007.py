n = int(input())
a = list(map(int,input().split()))
a.sort()
q = int(input())
b = [int(input()) for _ in range(q)]



for i in range(q):
  a_min = 0
  a_max = n-1
  a_mean = (n-1)//2
  while a_min != a_mean:
    if b[i] >= a[a_mean]:
      a_min = a_mean
    else:
      a_max = a_mean
    a_mean = (a_min+a_max)//2
  if a_mean != n-1:
    print(min(abs(a[a_mean]-b[i]), abs(a[a_mean+1]-b[i])))
  else:
    print(abs(a[a_mean]-b[i]))
