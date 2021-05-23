import sys

#input()
def I(): return sys.stdin.readline()
#int(input())
def II(): return int(sys.stdin.readline())
#map(int,input().split())
def MI(): return map(int, sys.stdin.readline().split())
#list(map(int,input().split()))
def LI(): return list(map(int, sys.stdin.readline().split()))
#行列
def LLI(rows_number): return [LI() for _ in range(rows_number)]