import sys

def cut(arr, mina, maxa):
    mida = (mina + maxa) // 2
    while mina < maxa:
        count = 0
        for i in arr:
            count += i // mida
        if count < N:
            maxa = mida - 1
            mida = (mina + maxa) // 2
        else:
            mina = mida
            mida = (mina + maxa) // 2 + 1
    return mina

K, N = map(int, sys.stdin.readline().split(' '))
lan = []
for i in range(K):
    lan.append(int(sys.stdin.readline()))

minL = 1
maxL = max(lan)
print(cut(lan, minL, maxL))