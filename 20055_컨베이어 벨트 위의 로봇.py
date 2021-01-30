from collections import deque, Counter
import sys
read = lambda: sys.stdin.readline().strip()

n, k = map(int, read().split())
belt = deque(list(map(int, read().split())))
robots = deque([])

cnt = Counter(belt)[0]
ans = 0

# 4. 내구도가 0인 칸의 개수가 k개 이상이라면 과정을 종료한다.
while cnt < k:
    ans += 1

    # 1. 벨트가 한 칸 회전한다.
    belt.rotate(1)
    for i in range(len(robots)):
        robots[i] += 1

    stack = []
    # 2. 가장 먼저 벨트에 올라간 로봇부터, 벨트가 회전하는 방향으로 한 칸 이동할 수 있다면 이동한다.
    #    만약 이동할 수 없다면 가만히 있는다.
    while robots:
        next_pos = robots.popleft() + 1

        if next_pos >= n:
            continue

        # 1. 로봇이 이동하기 위해서는 이동하려는 칸에 로봇이 없으며,
        if next_pos in stack:
            stack.append(next_pos - 1)
            continue

        #    그 칸의 내구도가 1 이상 남아 있어야 한다.
        if not belt[next_pos] >= 1:
            stack.append(next_pos - 1)
            continue

        stack.append(next_pos)
        belt[next_pos] -= 1
        if belt[next_pos] == 0:
            cnt += 1

    robots = deque(stack)

    # 3. 올라가는 위치에 로봇이 없다면 로봇을 하나 올린다.
    if 0 not in robots and belt[0] > 0:
        robots.append(0)
        belt[0] -= 1
        if belt[0] == 0:
            cnt += 1

print(ans)
