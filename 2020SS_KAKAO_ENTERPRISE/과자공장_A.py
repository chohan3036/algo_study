# 길이 같게, 최대한 길게, 여러 개
# 합치는 건 안 됨. 쪼개서 같은 길이의 여러 개로 만들어야 함
# n : 원래 개수 k : 만들어져야 하는 개수
# round(x, 2)
# 이분탐색인가?

n, k = map(int, input().split())
#snacks = []
#for _ in range(n):
#    snacks.append(float(input()))

#tc1
#snacks = [6.3, 4.3]

#tc2
snacks = [51.28,96.87,96.86,48.63,87.83,
        51.29,56.72,38.05,3.88,79.40,
        33.43,30.75,13.12,67.80,20.15,
        96.71,95.93,10.91]

cur_snacks = 0
start, end = 0, max(snacks)
mid = start + (end - start) / 2
while start <= end:  # 이분탐색하면서 몫만큼 더해, k될 때까지
    # mid 값으로 과자 쪼개서 만들기
    for s in snacks:
        cur_snacks += s // mid

    if cur_snacks > k:  # 너무 많이 만들었으니까 길이 늘림
        start = mid + 0.001  # 0.01하면 너무 큼.. 틀렸다

    elif cur_snacks < k:
        end = mid - 0.001

    else:
        break

    mid = start + (end - start) / 2
    cur_snacks = 0

print(format(round(mid + 0.01, 2), '.2f'))
