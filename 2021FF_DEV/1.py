# 0 이 모르는 숫자
# 0 다 틀리면 최저, 0 다 맞으면 최고
# 0 빼고 맞는 갯수 찾으면 됨


def solution(lottos, win_nums):
    best, worst = 0, 0
    for number in lottos:
        if number in win_nums:  # 숫자가 모두 유일하므로
            best += 1           # in 연산자로 검사
            worst += 1

        if number == 0:
            best += 1

    if worst < 2:
        worst = 1

    return [7 - best, 7 - worst]


print(solution([0, 9, 3, 45, 4, 35], [20, 9, 3, 45, 4, 35]))
