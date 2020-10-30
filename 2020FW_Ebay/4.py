from collections import deque
# 사람 : 식인종과 같거나 많은 수만큼 이동
# 식인종 : 사람과 같거나 적은 수만큼 이동


def bfs(a1, a2, b1, b2, lr, depth, p):
    q = deque([(a1, a2, b1, b2, lr, depth)])
    visited = set()
    visited.add((a1, a2, b1, b2))

    while q:
        x1, x2, y1, y2, lr, depth = q.popleft()

        # 다 옮겼으면 횟수 리턴
        if (x1, x2, y1, y2) == (0, 0, a1, a2):
            return depth

        # 배가 왼쪽섬
        if lr == 0:
            # 사람 옮기기
            for i in range(1, min(p, x1)):
                if x1 - i < 0:
                    break
                if 0 < x1 - i < x2:
                    continue
                x1 -= i

                if y1 + i < y2:
                    continue
                y1 += i

                q.append((x1, x2, y1, y2, 1, depth + 1))
                visited.add((x1, x2, y1, y2))

            # 식인종 옮기기
            for i in range(1, min(p, x2)):
                if x2 - i < 0:
                    break
                x2 -= i

                if y2 + i > y1:
                    continue
                y2 += i

                q.append((x1, x2, y1, y2, 1, depth + 1))
                visited.add((x1, x2, y1, y2))

        else:
            # 사람 옮기기
            for i in range(1, min(p, y1)):
                if y1 - i < 0:
                    break
                if 0 < y1 - i < y2:
                    continue
                y1 -= i

                if x1 + i < x2:
                    continue
                x1 += i

                q.append((x1, x2, y1, y2, 0, depth + 1))
                visited.add((x1, x2, y1, y2))

            # 식인종 옮기기
            for i in range(1, min(p, y2)):
                if y2 - i < 0:
                    break
                y2 -= i

                if x2 + i > x1:
                    continue
                x2 += i

                q.append((x1, x2, y1, y2, 0, depth + 1))
                visited.add((x1, x2, y1, y2))

    return -1


def solution(n, m, p):
    if m > p:
        return -1
    else:
        return bfs(n, m, 0, 0, 0, 0, p)


print(solution(2, 2, 2))
