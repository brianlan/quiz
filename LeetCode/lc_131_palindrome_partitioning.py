from common import *


class Solution:
    @staticmethod
    @lru_cache(maxsize=None)
    def is_palidromes(s: str) -> bool:
        n = len(s)
        if n == 0:
            raise ValueError("input string s can't be empty.")
        if n == 1:
            return True
        if n == 2:
            return s[0] == s[1]
        return (s[0] == s[-1]) and Solution.is_palidromes(s[1:-1])

    @staticmethod
    def find_heading_palindromes(s: str) -> List[Tuple[str, int]]:
        if len(s) == 0:
            raise ValueError("input string s can't be empty.")
        heading_palidromes = [(s[0], 1)] + [(s[:j], j) for j in range(2, len(s) + 1) if Solution.is_palidromes(s[:j])]
        return heading_palidromes

    def partition(self, s: str) -> List[List[str]]:
        logger.debug(f'\n"{s}"')
        n = len(s)
        cache = {"": [[]]}
        for i in range(n - 1, -1, -1):
            substr = s[i:]
            heading_palidromes = Solution.find_heading_palindromes(substr)
            new_partitions = []
            for head, pos in heading_palidromes:
                tail = substr[pos:]
                new_partitions.extend([[head] + v for v in cache[tail]])
            cache[substr] = new_partitions

        return cache[s]


if __name__ == '__main__':
    s = "".join([chr(97 + i) for i in np.random.randint(6, size=16)])
    # s = "abcbabaab"
    # s = "aab"
    logger.info(Solution().partition(s))

"""
1 2 3 4 5 6 7 8 9
a b c b a b a a b

f[9:9]: f['b'] = 'b' | EMPTY
==> ['b']

f[8:9]: f['ab'] = 'a' | f['b']
==> ['a', 'b']

f[7:9]: f['aab'] = 'a' | f['ab'], 'aa' | f['b']
==> ['a', 'a', 'b'], ['aa', 'b']

f[6:9]: f['baab'] = 'b' | f['aab'], 'baab' | EMPTY
==> ['b', 'a', 'a', 'b'], ['b', 'aa', 'b'], ['baab']

f[5:9]: f['abaab'] = 'a' | f['baab'], 'aba' | f['ab']
==> ['a', 'b', 'a', 'a', 'b'], ['a', 'b', 'aa', 'b'], ['a', 'baab'], ['aba', 'a', 'b']

f[4:9]: f['babaab'] = 'b' | f['abbab'], 'bab' | f['aab']
==> ['b', 'a', 'b', 'a', 'a', 'b'], ['b', 'a', 'b', 'aa', 'b'], ['b', 'a', 'baab'], ['b', 'aba', 'a', 'b'],
    ['bab', 'a', 'a', 'b'], ['bab', 'aa', 'b']

f[3:9]: f['cbabaab'] = 'c' | f['babaab']
==> ['c', 'b', 'a', 'b', 'a', 'a', 'b'], ['c', 'b', 'a', 'b', 'aa', 'b'], ['c', 'b', 'a', 'baab'], ['c', 'b', 'aba', 'a', 'b'],
    ['c', 'bab', 'a', 'a', 'b'], ['c', 'bab', 'aa', 'b'],

f[2:9]: f['bcbabaab'] = 'b' | f['cbabaab'], 'bcb' | f['abaab']
==> ['b', 'c', 'b', 'a', 'b', 'a', 'a', 'b'], ['b', 'c', 'b', 'a', 'b', 'aa', 'b'], ['b', 'c', 'b', 'a', 'baab'], ['b', 'c', 'b', 'aba', 'a', 'b'],
    ['b', 'c', 'bab', 'a', 'a', 'b'], ['b', 'c', 'bab', 'aa', 'b'],
    ['bcb', 'a', 'b', 'a', 'a', 'b'], ['bcb', 'a', 'b', 'aa', 'b'], ['bcb', 'a', 'baab'], ['bcb', 'aba', 'a', 'b']


f[1:9]: f['abcbabaab'] = 'a' | f['bcbabaab'], 'abcba' | f['baab']
==> ['a', 'b', 'c', 'b', 'a', 'b', 'a', 'a', 'b'], ['a', 'b', 'c', 'b', 'a', 'b', 'aa', 'b'], ['a', 'b', 'c', 'b', 'a', 'baab'], ['a', 'b', 'c', 'b', 'aba', 'a', 'b'],
    ['a', 'b', 'c', 'bab', 'a', 'a', 'b'], ['a', 'b', 'c', 'bab', 'aa', 'b'],
    ['a', 'bcb', 'a', 'b', 'a', 'a', 'b'], ['a', 'bcb', 'a', 'b', 'aa', 'b'], ['a', 'bcb', 'a', 'baab'], ['a', 'bcb', 'aba', 'a', 'b'],
    ['abcba', 'b', 'a', 'a', 'b'], ['abcba', 'b', 'aa', 'b'], ['abcba', 'baab']
"""