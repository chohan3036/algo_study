#n, m = map(int, input().split())
#num = list(map(int, input().split()))

n, m = 10, 5
num = [1, 2, 3, 4, 2, 5, 3, 1, 1, 2]

i, j = 0, 0
cnt = 0
psum = 0
while True:
    if psum >= m:
        psum -= num[j]
        j += 1
    elif i == n:
        break
    else:
        psum += num[i]
        i += 1

    if psum == m:
        cnt += 1

print(cnt)
