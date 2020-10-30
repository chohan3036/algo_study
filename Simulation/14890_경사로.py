def check(road):
    # 이미 경사로가 놓아져 있는지 검사
    visted = set()

    for i in range(1, n):
        # 바로 전 인덱스의 높이와 비교함
        tilt = road[i - 1]

        # 현재 인덱스와 이전 인덱스의 높이가 다를 때만 조건 검사
        if road[i] != tilt:
            # 낮 > 높 일 경우, 범위 체크
            if road[i] == tilt + 1 and i - l >= 0:
                for j in range(i - l, i):
                    # 경사로 길이만큼 같은 높이인지 검사
                    if not road[j] == tilt:
                        return False
                    # 경사로가 이미 놓아져 있는지 검사
                    if j not in visted:
                        visted.add(j)
                    else:
                        return False

            # 높 > 낮 일 경우, 범위 체크
            elif road[i] == tilt - 1 and i + l - 1 < n:
                for j in range(i, i + l):
                    # 경사로 길이만큼 같은 높이인지 검사
                    if not road[j] == road[i]:
                        return False
                    # 경사로가 이미 놓아져 있는지 검사
                    if j not in visted:
                        visted.add(j)
                    else:
                        return False
            else:
                return False

    return True


n, l = map(int, input().split())
mat = [list(map(int, input().split())) for _ in range(n)]

ans = 0
for i in range(n):
    if check(mat[i]):
        ans += 1

# 전치행렬 생성
tp = list(zip(*mat))
for i in range(n):
    if check(tp[i]):
        ans += 1

print(ans)
