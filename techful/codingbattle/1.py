import sys

#input()
def I(): return sys.stdin.readline().rstrip()
#list(input())
def SI(): return list(I())
#int(input())
def II(): return int(I())
#map(int,input().split())
def MI(): return map(int, I().split())
#map(str, input().split())
def MS(): return map(str, I().split())
#list(map(int,input().split()))
def LI(): return list(MI())
#行列
def LLI(rows_number): return [LI() for _ in range(rows_number)]
#文字の行列
def LSI(rows_number): return [SI() for _ in range(rows_number)]

n = II()
c = LI()

a = min(c)
al = [a]
bl = []

for i in range(n-1):
    c2 = LI()
    for j in range(n-1):
        b = c[j]-a
        if i == 1:
            bl.append(b)
        if c2[j]-b != c2[j+1]-b:
            print("No")
            exit()
    else:
        al.append(c2[0]-c[0]+a)
        
print(*al)
print(*bl)