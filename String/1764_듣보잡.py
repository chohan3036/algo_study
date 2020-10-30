import sys
read = lambda: sys.stdin.readline().strip()

N, M = map(int, read().split())
hear = set()
see = set()

for _ in range(N):
    hear.add(read())

for _ in range(M):
    see.add(read())

never = list(hear & see)
print(len(never))
for n in sorted(never):
    print(n)
