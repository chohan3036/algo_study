import sys
from collections import deque

readline = lambda: sys.stdin.readline().strip()

wheels = []
for i in range(4):
    wheels.append(deque())
    wheels[i] += map(int, readline())


def rotating(cur_wheel, idx, dir):
    left, right = 6, 2
    cur_pole = []
    for i in range(4):
        cur_pole.append((cur_wheel[i][left], cur_wheel[i][right]))

    flag = dir
    for i in range(idx, 0, -1):
        if cur_pole[i - 1][1] == cur_pole[i][0]:
            break
        flag *= -1
        cur_wheel[i - 1].rotate(flag)

    flag = dir
    for i in range(idx, 3, 1):
        if cur_pole[i][1] == cur_pole[i + 1][0]:
            break
        flag *= -1
        cur_wheel[i + 1].rotate(flag)


K = int(readline())
for _ in range(K):
    idx, dir = map(int, readline().split(' '))
    rotating(wheels, idx - 1, dir)
    wheels[idx - 1].rotate(dir)

score = 0
for i in range(4):
    pow = 2 ** i
    score += wheels[i][0] * pow
print(score)
