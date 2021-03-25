def flip(u):
    flipped = list(map(lambda x: '(' if x == ')' else ')', u[1: -1]))
    return ''.join(flipped)


print(flip("()))((()"))
