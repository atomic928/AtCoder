n = input()
if len(n)%2 == 0:
  if n[:len(n)//2] == n[:len(n)//2-1:-1]:
    print("Yes")
    exit()
else:
  if n[:(len(n)+1)//2-1] == n[:(len(n)+1)//2-1:-1]:
    print("Yes")
    exit()
for i in range(len(n)-1):
  n = "0" + n
  if len(n)%2 == 0:
    if n[:len(n)//2] == n[:len(n)//2-1:-1]:
      print("Yes")
      exit()
  else:
    if n[:(len(n)+1)//2-1] == n[:(len(n)+1)//2-1:-1]:
      print("Yes")
      exit()
print("No")