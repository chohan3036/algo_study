from itertools import permutations
list1 = [0,0,0, 0, 2]
perm = permutations(list1, len(list1))
set1 = set(perm)
print(set1)
perm2 = permutations(list1, len(list1))
for p in perm2:
    print(p, end='  ')