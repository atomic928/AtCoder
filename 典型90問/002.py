n = int(input())
l = ["()"]

lsave = [[] for _ in range(20)]
if n%2 == 0:
  if n == 2:
    print(l[0])
  else:
    for i in range((n-2)//2):
      tuika = []
      for kakko in l:
        tuika.append("("+kakko+")")
        tuika.append("()"+kakko)
        tuika.append(kakko+"()")
      
      if i > 1:
        for j in range(i-1):
          for pre1 in lsave[j]:
            for pre2 in lsave[i-j-2]:
              tuika.append(pre1+pre2)
      l = list(set(tuika))
      
      lsave[i] = l

    l.sort()
    for c in range(len(l)):
      print(l[c])
