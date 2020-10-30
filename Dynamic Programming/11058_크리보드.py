# 그냥 a 친거랑 선택, 복사, 붙여넣기 한 거랑 비교

n = int(input())
a = [-1] * (n + 1)
a[0] = 0

for i in range(1, n + 1):
    a[i] = a[i - 1] + 1
    for j in range(1, i - 2):
        a[i] = max(a[i], a[i - j - 2] * (j + 1))

print(a[n])
