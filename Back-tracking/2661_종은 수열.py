import sys


def bt(seq):
    end = len(seq)
    length = 0
    for i in range(end - 1, (end - 1) // 2, -1):
        length += 1
        if seq[i - length: i] == seq[i: i + length]:
            return

    if end == n:
        print(seq)
        sys.exit()

    bt(seq + '1')
    bt(seq + '2')
    bt(seq + '3')


n = int(input())
bt('')
