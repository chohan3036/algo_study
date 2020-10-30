import sys
from collections import deque
readline = lambda: sys.stdin.readline().strip()

N = int(readline())
card = deque([i + 1 for i in range(N)])

while len(card) > 1:
    card.popleft()
    if len(card) == 1:
        break
    card.rotate(-1)

print(card[0])
