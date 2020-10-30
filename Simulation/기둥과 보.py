def check(ans):
    for x, y, p_b in ans:
        # 기둥은 바닥 위에 있거나
        # 보의 한쪽 끝 부분 위에 있거나
        # 다른 기둥 위에 있거나
        if p_b == 0:
            if y == 0 or [x - 1, y, 1] in ans or [x, y, 1] in ans or [x, y - 1, 0] in ans:
                continue
            else:
                return False

        # 보는 한쪽 끝 부분이 기둥 위에 있거나
        # 양쪽 끝 부분이 다른 보와 동시에 연결되어 있거나
        elif p_b == 1:
            if [x, y - 1, 0] in ans or [x + 1, y - 1, 0] in ans or ([x - 1, y, 1] in ans and [x + 1, y, 1] in ans):
                continue
            else:
                return False
    return True


def solution(n, build_frame):
    answer = []

    for bf in build_frame:
        x, y, p_b, add_del = bf

        if add_del == 1:  # 설치
            answer.append([x, y, p_b])
            if not check(answer):
                answer.remove([x, y, p_b])
        else:  # 삭제
            answer.remove([x, y, p_b])
            if not check(answer):
                answer.append([x, y, p_b])

    return sorted(answer)


print(solution(5, [[0,0,0,1],[2,0,0,1],[4,0,0,1],[0,1,1,1],
                   [1,1,1,1],[2,1,1,1],[3,1,1,1],[2,0,0,0],
                   [1,1,1,0],[2,2,0,1]]))
