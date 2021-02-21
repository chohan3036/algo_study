import sys
read = lambda: sys.stdin.readline().strip()

n = int(read())
pop = list(map(int, read().split()))
area = []
for _ in range(n):
    