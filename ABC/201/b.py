from operator import itemgetter

n = int(input())
st = [list(map(str,input().split())) for _ in range(n)]
st = [[i[0], int(i[1])] for i in st]
st.sort(reverse=True, key = itemgetter(1))
print(st[1][0])

