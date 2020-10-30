letters = 'abcdefghijklmnopqrstuvwxyz'
dic = {}
for ch in letters:
    dic[ch] = 0
for s in input():
    dic[s] += 1
print(' '.join(map(str, dic.values())))


alphabet = ['a', 'b', 'c', 'd', 'e',
         'f', 'g', 'h', 'i', 'j',
         'k', 'l', 'm', 'n', 'o',
         'p', 'q', 'r', 's', 't',
         'u', 'v', 'w', 'x', 'y', 'z']
num_alphbet = [0 for _ in alphabet]
input_str = input()
for i in range(len(alphabet)-1):
    num_alphbet[i] += input_str.count(alphabet[i])

for x in num_alphbet:
    print(x, end=' ')
