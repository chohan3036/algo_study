cnt = 0
ans = []

while True:
    cnt += 1
    l, p, v = map(int, input().split())
    if not l and not p and not v:
        break
    camp = v // p * l + min(l, v % p)
    ans.append('Case {0}: {1}'.format(cnt, camp))

for a in ans:
    print(a)
