import sys
reading = lambda: sys.stdin.readline().strip()

string = list(reading())
c4 = list(reading())
i, j, k = 0, 0, 0
l1 = len(string)
l2 = len(c4)
stack = ['' for _ in range(l1)]
flag = False
cnt = 0

while i < l1:
    stack += string[i]
    i += 1
    if stack[j] == c4[k]:
        flag = True
        j += 1
        k += 1
        cnt += 1
        if k == l2:
            for _ in range(l2):
                stack.pop()
            j -= (l2 + cnt)
            k = 0
            cnt = 0
            flag = False
    else:
        if flag:
            j -= cnt - 1
            k = 0
            cnt = 0
            flag = False
        j += 1
        cnt = 0

print(stack if stack else 'FRULA')
