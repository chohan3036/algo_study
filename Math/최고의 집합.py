def solution(n, s):
    num = [s // n] * n
    if not all(num):
        return [-1]

    div = s % n
    for i in range(div):
        num[i % n] += 1

    num.sort()
    return num
