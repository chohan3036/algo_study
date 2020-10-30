import sys
read = lambda: sys.stdin.readline().strip()

people = 0
max_people = 0
for _ in range(4):
    t_off, t_on = map(int, read().split())
    people += t_on - t_off
    max_people = max(people, max_people)

print(max_people)
