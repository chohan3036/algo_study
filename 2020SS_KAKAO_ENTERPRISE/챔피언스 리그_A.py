from collections import defaultdict

n = int(input())
num_league = n * (n - 1)

num_wins = defaultdict(lambda: [0, 0])   # 승패 횟수와 세트 득실 기록

for _ in range(num_league):
    t1, s1, t2, s2 = map(str, input().split())
    s1, s2 = int(s1), int(s2)   # 점수 정수값으로 변환

    # 1. 승수 기록
    # 2. 세트 득실 따지기
    # 이긴 세트는 더하고, 진 세트는 뺌
    if s1 > s2:
        num_wins[t1][0] += 1

        num_wins[t1][1] += s1 - s2
        num_wins[t2][1] -= s1 - s2

    else:
        num_wins[t2][0] += 1

        num_wins[t2][1] += s2 - s1
        num_wins[t1][1] -= s2 - s1


num_wins = sorted(num_wins.items(), key=lambda x: (-x[1][0], -x[1][1], x[0]))
for t, wins in num_wins:
    tmp = ''
    tmp += t
    for w in wins:
        tmp += ' ' + str(w)
    print(tmp)
