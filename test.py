for i in range(11):
    print(i, end=' ')
    print(i - (i & -i))