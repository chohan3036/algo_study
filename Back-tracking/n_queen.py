# 규칙
# 1. 한 줄에 하나만 올 수 있음
# 2. i번째 전 말 +/- (N + 1) 자리에 올 수 없음
#
N = int(input())
board = [[False] * N] * N
print(board)
count = 0

def chess(depth, list, N):
    if depth == N:
        return

    for i in range(N):
        list[i] = True
        chess(depth+1,list[])