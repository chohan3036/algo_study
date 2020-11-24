import sys
read = lambda: sys.stdin.readline().strip()
from itertools import combinations

while True:
    numbers = list(map(int, read().split()))
    if numbers == [0]:
        break
    cases = []
    for x in combinations(numbers[1:], numbers[0]):
        for lotto in combinations(x, 6):
            if lotto not in cases:
                cases.append(lotto)

    cases.sort()
    for case in cases:
        print(' '.join([str(x) for x in case]))

    print()
