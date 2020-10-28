from collections import deque


def bfs(bg, tg, depth, words):
    q = deque([(bg, depth)])
    visit = set()
    visit.add(bg)

    while q:
        cw, cd = q.popleft()
        if cw == tg:
            return cd

        for nw in words:
            if nw in visit:
                continue

            cnt = 0
            for i in range(len(cw)):
                if cw[i] != nw[i]:
                    cnt += 1

                if cnt > 1:
                    break

            if cnt > 1:
                continue

            q.append((nw, cd + 1))
            visit.add(nw)

    return 0


def solution(begin, target, words):
    step = bfs(begin, target, 0, words)
    return step


if __name__ == "__main__":
    print(solution("hit", "cog", ["hot", "dot", "dog", "lot", "log"]))
