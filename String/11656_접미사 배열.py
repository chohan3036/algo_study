import sys
read = lambda: sys.stdin.readline().strip()

string = read()
tails = []
for i in range(len(string)):
    tails.append(string[i:])

tails.sort()
for t in tails:
    print(t)
