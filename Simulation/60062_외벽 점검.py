# 아니구나 거리를 쪼개줘야 돼..
# 차이가 가장 적은 인덱스를 끝으로 해서 거리 재기
# 뭔가 rotate 써야될 것 같은..
from collections import deque
from itertools import permutations
from copy import deepcopy


def solution(n, weak, dist):
    dist.sort(reverse=True)

    weak = deque(weak)
    weaks = [deepcopy(weak)]
    for i in range(len(weak) - 1):
        weak.rotate(-1)
        weak[-1] += 12
        weaks.append(deepcopy(weak))
    print(weaks)

    for i in range(1, len(dist) + 1):
        can = permutations(dist[: i])
        print(can)

        for c in can:
            f_idx, f_cnt = 0, 1
            reach = weaks[i][0] + c[f_idx]

            for idx in range(len(weak)):
                if weaks[i][idx] > reach:
                    f_cnt += 1

                    if f_cnt > len(can):
                        break

                    f_idx += 1
                    reach = can[f_idx] + weaks[i][idx]

    return weak


print(solution(12, [1, 5, 6, 10], [1, 2, 3, 4]))
