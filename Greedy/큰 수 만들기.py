number = input()
k = int(input())

ans = []
for n in number:
    while ans and ans[-1] < n and k > 0:
        ans.pop()
        k -= 1
    ans.append(n)

ans = ans if k == 0 else ans[: -k]
print(''.join(ans))
