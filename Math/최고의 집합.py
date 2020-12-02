# 와.. 곱이 가장 크려면 표준편차가 가장 작아야 한다

def solution(n, s):
    num = [s // n] * n
    div = s % n
    for i in range(div):
        num[i % n] += 1

    num.sort()
    return num


print(solution(2, 1))
