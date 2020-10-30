k = []
S = []
temp = []
for i in range(10):
    temp = input()
    if temp == '0': break
    S.append(list(map(int, temp.split(' '))))
    k.append(S[i].pop(0))
    print(k, S)

def dfs(list, cnt):
    if cnt == 6:
        print()

    print(list.pop(0), end='')
    dfs(list, cnt+1)