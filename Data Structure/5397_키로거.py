import sys
read = lambda: sys.stdin.readline().strip()
from collections import deque

n = int(read())
#pw_str = [read() for _ in range(n)]
pw_str = 'A<<S-D-SDA<S>>-A<-<<>AAQW><EQ-'
for i in range(n):
    front, back = deque([]), deque([])
    for k in pw_str[i]:
        if k == '<':
            if front:
                back.appendleft(front.pop())
        elif k == '>':
            if back:
                front.append(back.popleft())
        elif k == '-':
            if front:
                front.pop()
        else:
            front.append(k)
    front.extend(back)
    print(''.join(front))
