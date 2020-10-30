import sys
from queue import PriorityQueue

N = int(sys.stdin.readline())
q = PriorityQueue()
answer = []

for i in range(N):
    x = int(sys.stdin.readline())
    if x == 0:
        if q.empty():
            answer.append(0)
        else:
            answer.append(q.get())
    else:
        q.put(x)

for str in answer:
    print(str)