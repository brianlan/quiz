import sys
from collections import defaultdict

def read_input():
    lines = [l.strip() for l in sys.stdin]
    n, m = map(int, lines[0].split())
    meat = [list(map(int, l.split())) for l in lines[1:]]
    return m, meat

m, meat = read_input()
# 如果m为0，即手速无限快，则所有的肉都可以吃到
if m == 0:
    print(len(meat))

# 根据没块肉的x和y得到每个有美味肉的时刻，肉的数量是多少
meat_info = defaultdict(int)
for x, y in meat:
    meat_info[x+y] += 1

last_meat_time = max(meat_info.keys())
opt = [0] * (last_meat_time + m + 1)

# 动态规划的思想：每个时刻的最多肉的个数opt[i]=has_meat[i]+opt[i+m]
for i in range(last_meat_time, 0, -1):
    if i in meat_info.keys():
        has_meat = 1
    else:
        has_meat = 0
    opt[i] = has_meat + opt[i+m]
print(opt[1])

"""
3 1
1 2
1 3
2 3
"""