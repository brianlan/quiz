from typing import List
from functools import cmp_to_key


def compare(a: str, b: str) -> int:
    if a + b > b + a:
        return 1
    elif a + b < b + a:
        return -1
    else:
        return 0


class Solution:
    def minNumber(self, nums: List[int]) -> str:
        """
        若拼接字符串 x + y > y + xx+y>y+x ，则 m > nm>n ；
        反之，若 x + y < y + xx+y<y+x ，则 n < mn<m ；
        根据以上规则，套用任何排序方法对 numsnums 执行排序即可。
        """
        sorted_nums = sorted(map(str, nums), key=cmp_to_key(compare))
        return ''.join(sorted_nums)


if __name__ == "__main__":
    print(Solution().minNumber([36,32,3,30,35,5,9,2,4,41]))