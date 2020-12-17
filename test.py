import re
from collections import Counter

s = "{{2},{2,1},{2,1,3},{2,1,3,4}}"
num = Counter(re.findall("\d+", s))
ans = sorted(num.items(), key=lambda x: -x[1])
ans = [int(x[0]) for x in ans]
print(ans)
