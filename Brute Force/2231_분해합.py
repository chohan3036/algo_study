# 생성자가 될 수 있는 요건
# 1. N보다 작아야 함
N = int(input())
n = int(N*0.8)
found = False

for i in range(n, N):
    sum = i
    div = i
    for j in range(7):
        sum += div % 10
        div //= 10
        if div == 0: break

    if sum == N:
        found = True
        break

if found == True: print(i)
else: print(0)