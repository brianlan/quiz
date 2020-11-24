"""
10. 正则表达式匹配
给你一个字符串 s 和一个字符规律 p，请你来实现一个支持 '.' 和 '*' 的正则表达式匹配。

'.' 匹配任意单个字符
'*' 匹配零个或多个前面的那一个元素
所谓匹配，是要涵盖 整个 字符串 s的，而不是部分字符串。

 
示例 1：

输入：s = "aa" p = "a"
输出：false
解释："a" 无法匹配 "aa" 整个字符串。
示例 2:

输入：s = "aa" p = "a*"
输出：true
解释：因为 '*' 代表可以匹配零个或多个前面的那一个元素, 在这里前面的元素就是 'a'。因此，字符串 "aa" 可被视为 'a' 重复了一次。
示例 3：

输入：s = "ab" p = ".*"
输出：true
解释：".*" 表示可匹配零个或多个（'*'）任意字符（'.'）。
示例 4：

输入：s = "aab" p = "c*a*b"
输出：true
解释：因为 '*' 表示零个或多个，这里 'c' 为 0 个, 'a' 被重复一次。因此可以匹配字符串 "aab"。
示例 5：

输入：s = "mississippi" p = "mis*is*p*."
输出：false
 

提示：

0 <= s.length <= 20
0 <= p.length <= 30
s 可能为空，且只包含从 a-z 的小写字母。
p 可能为空，且只包含从 a-z 的小写字母，以及字符 . 和 *。
保证每次出现字符 * 时，前面都匹配到有效的字符
"""


class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        if s and not p:
            return False
        if not s and not p:
            return True
        pattern = []
        i = 0
        while i < len(p):
            if p[i] == "*":
                pattern.append(p[i - 1 : i + 1])
                i += 2
                continue
            elif i > 0:
                pattern.append(p[i - 1])
            i += 1
        if p[-1] != "*":
            pattern.append(p[-1])
        match = [[False] * (len(pattern) + 1) for _ in range((len(s) + 1))]
        match[0][0] = True
        for i in range(0, len(s) + 1):
            for j in range(1, len(pattern) + 1):
                if pattern[j - 1].endswith("*"):
                    is_match = (
                        match[i][j - 1]
                        or match[i - 1][j]
                        and (s[i - 1] == pattern[j - 1][0] or pattern[j - 1][0] == ".")
                    )
                else:
                    try:
                        is_match = match[i - 1][j - 1] and (
                            s[i - 1] == pattern[j - 1] or pattern[j - 1] == "."
                        )
                    except IndexError:  # meaning s is an empty string.
                        is_match = False
                match[i][j] = is_match
        return match[-1][-1]


if __name__ == "__main__":
    assert not Solution().isMatch("a", "ab*a")
    assert Solution().isMatch("mississippi", "mis*i*sj*.*p*i*p*")
    assert not Solution().isMatch("", ".")
    assert Solution().isMatch("", "")
    assert Solution().isMatch("", ".*")
    assert not Solution().isMatch("a", "")
    assert not Solution().isMatch("aa", "a")
    assert Solution().isMatch("aa", "a*")
    assert Solution().isMatch("ab", ".*")
    assert Solution().isMatch("aab", "c*a*b")
    assert not Solution().isMatch("mississippi", "mis*is*p*.")
