import sys
read = lambda: sys.stdin.readline().strip()


def back_tracking(word, target):
    global avail, ans

    if len(word) == target:
        ans.add(word)
        return

    for a in avail:
        if avail[a] > 0:
            avail[a] -= 1
            back_tracking(word + a, target)
            avail[a] += 1


n = int(read())
words = [read() for _ in range(n)]
for i in range(n):
    avail = dict()
    ans = set()

    for char in words[i]:
        if char not in avail:
            avail[char] = 1
        else:
            avail[char] += 1

    back_tracking('', len(words[i]))
    for a in sorted(ans):
        print(''.join(a))
