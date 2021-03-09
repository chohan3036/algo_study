'''
from collections import Counter


def solution(n, computers):
    networks = [i for i in range(n)]
    for i in range(n):
        for j in range(n):
            if computers[i][j]:                     # i와 j가 같은 네트워크인데
                for k in range(n):
                    if networks[i] == networks[k]:  # i와 k가 같은 네트워크라면
                        networks[k] = networks[j]   # k와 j도 같은 네트워크

    return len(Counter(networks).keys())
'''


def dfs(n, computers, prev_node, networks):
    for i in range(n):
        if computers[prev_node][i] and networks[i] == 0:
            networks[i] = 1
            dfs(n, computers, i, networks)
    return networks


def solution(n, computers):
    networks = [0] * n
    for i in range(n):
        if networks[i] == 0:
            network = dfs(n, computers, i, [0] * n)
            for j in range(n):
                if networks[j] == 0:
                    networks[j] = network[j] * (i + 1)
    return len(set(networks))


print(solution(6, [[1, 0, 1, 1, 0, 0],
                   [0, 1, 0, 0, 1, 1],
                   [1, 0, 1, 1, 1, 1],
                   [1, 0, 1, 1, 1, 1],
                   [0, 1, 1, 1, 1, 1],
                   [0, 1, 1, 1, 1, 1]]))
