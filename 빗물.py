h, w = map(int, input().split())
walls = list(map(int, input().split()))

left, right = walls[0], max(walls[1:])
ans = 0
for i in range(1, w):
    left = max(left, walls[i])
    right = max(walls[i:])
    min_ = min(left, right)
    ans += min_ - walls[i]

print(ans)

# rain_sum, rain = 0, 0
# pre_wall = walls[0]
# for i in range(1, w):
#     # 맨 마지막에 벽이 짧은지 검사
#     if i == w - 1 and pre_wall > walls[i]:
#         rain_sum += rain * walls[i] - sum(walls[i - rain: i])
#         break
#     if pre_wall <= walls[i]:
#         rain_sum += rain * pre_wall - sum(walls[i - rain: i])
#         rain = 0
#         pre_wall = walls[i]
#     else:
#         rain += 1
#
# print(rain_sum)
