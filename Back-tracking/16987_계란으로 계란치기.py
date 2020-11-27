import sys
read = lambda: sys.stdin.readline().strip()


def egg_break(idx):
    global max_cnt

    if idx > len(eggs) - 1:
        cnt = 0
        for i in range(len(eggs)):
            if eggs[i][0] <= 0:
                cnt += 1
        max_cnt = max(max_cnt, cnt)
        return

    if eggs[idx][0] <= 0:
        egg_break(idx + 1)

    else:
        flag = False

        for i in range(len(eggs)):
            if idx == i or eggs[i][0] <= 0:
                continue

            flag = True
            # 계란 치기
            eggs[idx][0] -= eggs[i][1]
            eggs[i][0] -= eggs[idx][1]

            egg_break(idx + 1)

            # 계란 원상복구
            eggs[idx][0] += eggs[i][1]
            eggs[i][0] += eggs[idx][1]

        if not flag:
            egg_break(idx + 1)


n = int(read())
eggs = [list(map(int, read().split())) for _ in range(n)]
max_cnt = 0
egg_break(0)
print(max_cnt)
