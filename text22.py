from queue import PriorityQueue

q = PriorityQueue()
q.put((3, 4))
q.put((2, 6))
q.put((3, 5))
print(q.get())
print(q.get())
print(q.get())