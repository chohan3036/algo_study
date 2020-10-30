def facto(n):
    if n == 0 or n == 1:
        return n
    else:
        return n * facto(n-1)

N, K = map(int, input().split())
if K < 0 or K >= N:
    bin = 0
else:
    bin = int(facto(N) / (facto(K) * facto(N-K)))
print(bin % 1000000007)