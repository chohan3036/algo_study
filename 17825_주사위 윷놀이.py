from itertools import product

turns = list(map(int, input().split()))

# board 를 red 와 blue 로 나누어서 생성
red = [i for i in range(2, 42, 2)]
blue = [[10, 13, 16, 19, 25, 30, 35],
        [20, 22, 24, 25, 30, 35],
        [30, 28, 27, 26, 25, 30, 35],
        [40]]

# 점수를 저장할 전역변수
score = 0


def move(x, y, c):
    mx, my, mc = x, y + cur_turn, c
    if c == 0:
        if my in [4, 9, 14, 19]:                    # 10, 20, 30, 40 에서 blue 로 이동시킴
            mx, my, mc = (red[my] // 10) - 1, 0, 1  # 10 으로 나눈 몫으로 blue 의 행 결정
        if my > 19:                                 # 40 넘어가면 시작점으로
            mx, my, mc = 0, -1, 0
    else:
        if my > len(blue[mx]):                  # 40 넘어가면 시작점으로
            mx, my, mc = 0, -1, 0
        elif my == len(blue[mx]):               # 40 에서 경로 모아주기
            mx, my, mc = 3, 0, 1                # 40 을 blue 의 각 행에 두지 않고
                                                # blue 의 4 행에만 둠
    return mx, my, mc


# product 로 모든 경우의 수를 생성
orders = product([0, 1, 2, 3], repeat=10)

for order in orders:
    # 각 order 에 쓰일 변수들
    pieces = [(0, -1, 0)] * 4
    flag = True
    cur_score = 0

    for cur_piece, cur_turn in zip(order, turns):
        cx, cy, cc = pieces[cur_piece]
        nx, ny, nc = move(cx, cy, cc)

        # 시작점에 돌아갔으면 점수 합산 안 하고 다음 말로
        if (nx, ny, nc) == (0, -1, 0):
            pieces[cur_piece] = (0, -1, 0)
            continue

        # 이동할 칸에 이미 다른 말이 있으면 무효판 처리
        if (nx, ny, nc) in pieces:
            flag = False
            break

        # 말의 위치를 갱신
        pieces[cur_piece] = (nx, ny, nc)

        # 색에 따라 점수 합산
        if nc == 0:
            cur_score += red[ny]
        else:
            cur_score += blue[nx][ny]

    # 무효판이 아니고 이번 점수가 더 높을 때에만 갱신
    if flag and score < cur_score:
        score = cur_score

print(score)
