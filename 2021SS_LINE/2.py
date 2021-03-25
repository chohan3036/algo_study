# 길이 <= 100,000
from collections import Counter


def solution(inp_str):
    against = []
    c = Counter(inp_str)

    # 1번
    if not 8 <= len(inp_str) <= 15:
        against.append(1)

    kinds = [0] * 4
    # 2번
    for char in c:
        second = [0] * 4
        if ord(char) in range(65, 91):
            second[0] += 1
            kinds[0] += 1
        if ord(char) in range(97, 123):
            second[1] += 1
            kinds[1] += 1
        if ord(char) in range(48, 58):
            second[2] += 1
            kinds[2] += 1
        if char in '~!@#$%^&*':
            second[3] += 1
            kinds[3] += 1

        if 1 not in second and 2 not in against:
            against.append(2)

    # 3번
    if Counter(kinds)[0] > 1:
        against.append(3)

    # 4번
    forth = 1
    for i in range(len(inp_str) - 1):
        if inp_str[i] == inp_str[i + 1]:
            forth += 1
            if forth >= 4:
                against.append(4)
                break
        else:
            forth = 1

    # 5번
    for val in c.values():
        if val >= 5:
            against.append(5)
            break

    if against:
        return against
    else:
        return [0]


print(solution("CaCbCgCdC888834A"))
