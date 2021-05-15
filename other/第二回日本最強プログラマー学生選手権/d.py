n, p = map(int,input().split())

ans = ((p-1)*pow(p-2,n-1,10**9+7))%(10**9+7)

print(ans)