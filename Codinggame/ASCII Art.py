import sys
read = lambda: sys.stdin.readline()

l = int(read().strip())
h = int(read().strip())
t = list(read().strip())
words = [ord(x.upper()) - 65 if ord(x.upper()) - 65 >= 0 else 26 for x in t]
print(words)
ascii_list = [['' for _ in range(27)] for _ in range(h)]
for i in range(h):
    row = read()
    for j in range(27):
        ascii_list[i][j] += row[j * l: j * l + l]

for i in range(h):
    for j in range(len(t)):
        print(ascii_list[i][words[j]], end='')
    print()
