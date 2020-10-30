import sys

reading = lambda :sys.stdin.readline().strip()

A, B = reading().split()
len_A = len(A)
len_B = len(B)
_min = 50

for i in range(len_B - len_A + 1):
    cnt = 0
    for j in range(len_A):
        if A[j] != B[i + j]:
            cnt += 1
    _min = min(cnt, _min)

print(_min)