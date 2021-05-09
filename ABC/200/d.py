from itertools import combinations

n = int(input())
a = list(map(int, input().split()))
check = [[] for _ in range(200)]

flag = 0

for i in range(1, len(a)):
  for conb in combinations(a, i):
    if check[sum(conb)%200] == []:
      check[sum(conb)%200] = list(conb)
    else:
      ansb = [str(i) for i in check[sum(conb)%200]]
      ansc = [str(i) for i in list(conb)]
      ansb = [str(a.index(int(i))+1) for i in ansb]
      ansc = [str(a.index(int(i))+1) for i in ansc]
      if len(ansb) == len(ansc):
        if ansb != ansc:
          flag = 1
      else:
        flag = 1
      if flag:
        print("Yes")
        print(len(ansb), " ".join(ansb))
        print(len(ansc), " ".join(ansc))
        exit()

print("No")