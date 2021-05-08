from itertools import combinations

n = int(input())
a = list(map(int, input().split()))
check = [[] for _ in range(200)]

flag = 1

for i in range(1, len(a) + 1):
  for conb in combinations(a, i):
    if check[sum(conb)%200] == []:
      check[sum(conb)%200] = list(conb)
    else:
      ansb = [str(i) for i in check[sum(conb)%200]]
      ansc = [str(i) for i in list(conb)]
      ansb = [str(a.index(int(i))+1) for i in ansb]
      ansc = [str(a.index(int(i))+1) for i in ansc]
      if len(ansb) < len(ansc):
        for i in range(len(ansb)):
          if ansb[i] == ansc[i]:
            flag = 0
            break
          if i == len(ansb)-1:
            flag = 1
      else:
        for i in range(len(ansc)):
          if ansb[i] == ansc[i]:
            flag = 0
            break
          if i == len(ansc)-1:
            flag = 1
      if flag:
        print("Yes")
        print(len(ansb), " ".join(ansb))
        print(len(ansc), " ".join(ansc))
        exit()

print("No")