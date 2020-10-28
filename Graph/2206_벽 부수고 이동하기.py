import sys
read = lambda: sys.stdin.readline().strip()

n, m = map(int, read().split())
mat = [[0,1,0,0],
       [1,1,1,0],
       [1,0,0,0],
       [0,0,0,0],
       [0,1,1,1],
       [0,0,0,0]]

