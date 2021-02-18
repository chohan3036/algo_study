'''
k = int(input()) - 1
cnt = 0

while k > 0:
    cnt += k & 1
    k >>= 1

print(cnt & 1)
'''


def thue_morse(x):
    bin_str = bin(x)[2:]
    reverse = 0
    for i in bin_str[:-1]:
        if int(i):
            reverse += 1

    if reverse % 2 == 0:
        return int(bin_str[-1])
    else:
        return 1 - int(bin_str[-1])


k = int(input()) - 1
print(thue_morse(k))
