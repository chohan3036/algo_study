def volume():
    num = int(input())
    weight = []
    height = []

    for n in range(num):
        w, h = tuple(map(int, input().split(' ')))
        weight.append(w)
        height.append(h)
    rank = ([0 for i in range(num)])

    for i in range(num):
        rank[i] += 1
        for j in range(num):
            if weight[i] < weight[j]:
                if height[i] < height[j]:
                    rank[i] += 1
        print(rank[i], '', end='')

volume()
