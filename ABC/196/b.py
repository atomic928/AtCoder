import re
x = input()
ansm = re.search("\d+", x)
ans = ansm.group()
print(ans)