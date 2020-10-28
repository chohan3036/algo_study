#n, s = map(int, input().split())
#seq = list(map(int, input().split()))
n, s = 10, 15
seq = [5, 1, 3, 5, 10, 7, 4, 9, 2, 8]


ans = 1e9
left, right, part_sum, cnt = 0, 0, 0, 0

while left < len(seq):
    if part_sum >= s:
        ans = min(ans, cnt)
        part_sum -= seq[left]
        left += 1
        cnt -= 1
    else:
        if right == n:
            break
        part_sum += seq[right]
        right += 1
        cnt += 1
    print(left, right, cnt)

print(ans if ans != 1e9 else 0)
