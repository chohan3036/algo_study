from collections import deque


def solution(board, moves):
    # board 를 접근하기 쉽게 조작
    # 접근을 쉽게 하기 위해 전치행렬로 만듦
    # 빈 공간을 없애 바로 popleft 할 수 있게 만듦
    trans_board = [list(x) for x in zip(*board)]
    final_board = deque([])
    for i in range(len(board)):
        final_board.append(deque(map(int, [x for x in trans_board[i] if x != 0])))

    stack = []
    moves = deque(moves)
    cnt = 0
    while moves:
        cur_move = moves.popleft() - 1
        if final_board[cur_move]:
            cur_doll = final_board[cur_move].popleft()
        else:
            continue
        if stack and stack[-1] == cur_doll:
            stack.pop()
            cnt += 2
        else:
            stack.append(cur_doll)

    return cnt


print(solution([[0,0,0,0,0],[0,0,1,0,3],[0,2,5,0,1],[4,2,4,4,2],[3,5,1,3,1]], [1, 5, 3, 5, 1, 2, 1, 4]))