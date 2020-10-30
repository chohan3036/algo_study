# 다이나믹으로 풀 수도 있고 bfs 로도 풀 수 있음
# 뒤에서부터 채우는 이유!! : 리스트가 이미 다른 값으로 갱신이 돼 있는 상태라면
# 물건이 중복되어 고려될 수 있음!!
n, k = map(int, input().split())
goods = [tuple(map(int, input().split())) for _ in range(n)]
bag = [0] * (k + 1)

for i in range(n):
    for w in range(k, 1, -1):
        if w >= goods[i][0]:
            bag[w] = max(bag[w], bag[w - goods[i][0]] + goods[i][1])

print(bag[k])
