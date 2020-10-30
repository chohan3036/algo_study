import sys
reading = lambda :sys.stdin.readline().strip()

N = int(reading())
A = list(map(int, reading().split()))
S = int(reading())
cnt = 0

for i in range(N):
    for j in range(1, N):
        if A[j - 1] < A[j]:
            temp = A[j - 1]
            A[j - 1] = A[j]
            A[j] = temp
            cnt += 1
        if cnt >= S:
            break
    if cnt >= S:
        break

for i in range(N):
    if i <= N - 1:
        print(A[i], end=' ')
    else:
        print(A[i])