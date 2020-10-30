n, k, i = map(int, input().split())
cnt = 0
while k != i:
    k -= k // 2
    i -= i // 2
    cnt += 1
print(cnt if cnt > 0 else -1)