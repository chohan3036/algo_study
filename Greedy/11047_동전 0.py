num, money = map(int, input().split(' '))
values = []
count = 0
for i in range(num):
    values.append(int(input()))

for i in range(num-1, -1, -1):
    if money > 0:
        if money >= values[i]:
            count += money // values[i]
            money %= values[i]
print(count)