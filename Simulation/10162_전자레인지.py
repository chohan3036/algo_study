t = int(input())
sec = [300, 60, 10]
ans = [0, 0, 0]

for i in range(3):
    ans[i] = t // sec[i]
    t %= sec[i]

print(' '.join(map(str, ans))) if t == 0 else print(-1)
