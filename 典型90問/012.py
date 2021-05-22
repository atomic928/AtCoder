h, w = map(int,input().split())
Q = int(input())

p = [-1]*(h*w)
check = [[False]*(w+2) for _ in range(h+2)] #±1について調べるので端をFalseにしておく

def find(x):
    if p[x] == -1:
        return x
    else:
        p[x] = find(x)
        return p[x]

def unite(x, y):
    x = find(x)
    y = find(y)
    if x == y: return
    p[x] = y

def same(x, y):
    return find(x) == find(y)

for i in range(Q):
    q = list(map(int,input().split()))
    if q[0] == 1:
        r, c = q[1], q[2]
        check[r][c] = True
        if check[r-1][c]:
            unite((r-1)*w+c-1, (r-2)*w+c-1)
        if check[r+1][c]:
            unite((r-1)*w+c-1, r*w+c-1)
        if check[r][c-1]:
            unite((r-1)*w+c-1, (r-1)*w+c-2)
        if check[r][c+1]:
            unite((r-1)*w+c-1, (r-1)*w+c)
    else:
        r1, c1, r2, c2 = q[1], q[2], q[3], q[4]
        if same(r1*w+c1, r2*w+c2):
            print("Yes")
        else:
            print("No")
