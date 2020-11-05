import sys
read = lambda: sys.stdin.readline().strip()

for _ in range(int(read())):
    n, m = map(int, read().split())
    a = list(map(int, read().split()))
    b = list(map(int, read().split()))
    a.sort(reverse=True)
    b.sort(reverse=True)
    i = j = 0
    for _ in range()