from common import *

class Solution:
    def longestSubstring(self, s: str, k: int) -> int:
        logger.debug(f'\n"{s}"\n{k}')
        # find longest substring under different assumptions on distinct kinds of chars in it.
        valid_strs = []
        max_distinct_kinds = len(set(s))
        for m in range(1, max_distinct_kinds + 1):
            valid_strs.extend(self.find_longest_substring(s, k, m))
        if valid_strs:
            return max([len(i) for i in valid_strs])
        return 0

    def find_longest_substring(self, s: str, k: int, m: int) -> int:
        # logger.debug(f"\n{m=}")
        n = len(s)
        l, r = 0, 1
        valid_strs = []
        char_stats = defaultdict(int)
        char_stats[s[l]] = 1
        while True:
            if (r == n) or (len(char_stats) == m and s[r] not in char_stats):
                # logger.debug(f"\n{s[l:r]}")

                # if meet the criterion of k, add it to valid_strs
                if all([cnt >= k for _, cnt in char_stats.items()]):
                    valid_strs.append(s[l:r])
                
                if r == n:
                    break

                # move l towards right, to reduce char kinds in the window
                while True:
                    char_stats[s[l]] -= 1
                    if char_stats[s[l]] == 0:
                        del char_stats[s[l]]
                        l += 1
                        break
                    l += 1
            
            # add s[r] to the window
            char_stats[s[r]] += 1
            r += 1
        
        return valid_strs


class Solution2:
    """
    作者：fuxuemingzhu
    链接：https://leetcode-cn.com/problems/longest-substring-with-at-least-k-repeating-characters/solution/jie-ben-ti-bang-zhu-da-jia-li-jie-di-gui-obla/
    来源：力扣（LeetCode）
    著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。
    """
    def longestSubstring(self, s, k):
        """A much clean way of implementation."""
        if len(s) < k:
            return 0
        for c in set(s):
            if s.count(c) < k:
                return max(self.longestSubstring(t, k) for t in s.split(c))
        return len(s)


if __name__ == "__main__":
    # s, k = "aaebbacbcad", 2
    s, k = "a", 1
    # s, k = "aaaaaaaabbbbbbbbbbb", 1
    s, k = "".join([chr(97 + i) for i in np.random.randint(26, size=100)]), np.random.randint(5) + 1
    logger.info(Solution().longestSubstring(s, k))
