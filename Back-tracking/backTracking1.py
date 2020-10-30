N, M = map(int, input().split())
visited = [False] * N  # 탐사 여부 check
out = []  # 출력 내용

def dfs(depth, idx, N, M):
    if depth == M:  # 탈출 조건
        print(' '.join(map(str, out)))  # list를 str으로 합쳐 출력
        return
    for i in range(idx, N):  # 탐사 check 하면서
        if not visited[i]:  # 탐사 안했다면
            #visited[i] = True  # 탐사 시작(중복 제거)
            out.append(i+1)  # 탐사 내용
            dfs(depth+1, i, N, M)  # 깊이 우선 탐색
            #visited[i] = False  # 깊이 탐사 완료
            out.pop()  # 탐사 내용 제거

dfs(0, 0, N, M)