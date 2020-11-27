# 스타트와 링크
# 인원에서 구할 수 있는 조합 일일히 구하고
# 거기에서 또 일일히 시너지 값 더해 줌
# 백트랙킹으로 풀었어야 함
# visit 일차원 배열로 만들어서 chk
import sys
read = lambda: sys.stdin.readline().strip()


def dfs(stt, depth):
    global min_diff

    if depth == n // 2:
        team_a = team_b = 0
        for i in range(n):
            for j in range(n):
                if not team[i] and not team[j]:
                    team_a += synergy[i][j]
                elif team[i] and team[j]:
                    team_b += synergy[i][j]
        min_diff = min(min_diff, abs(team_a - team_b))

    for i in range(stt, n):
        if not team[i]:
            team[i] = 1
            dfs(i + 1, depth + 1)
            team[i] = 0


n = int(read())
synergy = [list(map(int, read().split())) for _ in range(n)]

team = [0 for _ in range(n)]
min_diff = sys.maxsize

dfs(0, 0)
print(min_diff)
