import sys
reading = lambda :sys.stdin.readline().strip()

N = list(map(int, reading().split()))
n = 5

for i in range(n):
    for j in range(1, n):
        if N[j - 1] > N[j]:
            temp = N[j - 1]
            N[j - 1] = N[j]
            N[j] = temp
            for k in N:
                print(k, end=' ')
            print()