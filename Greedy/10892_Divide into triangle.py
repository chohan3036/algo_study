import sys
read = lambda: sys.stdin.readline().strip()

N = int(read())
pile = [0]
for _ in range(N * 3):
    pile.append(tuple(map(int, read().split())))


print(pile)
