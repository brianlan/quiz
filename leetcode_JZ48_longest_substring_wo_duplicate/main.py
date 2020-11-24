class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        s = '' if s is None else s
        i, j = 0, 0
        longest_substr = ''
        substr = []
        while j <= len(s):
            if len(set(substr)) < len(substr):
                i += 1 + substr.index(s[j - 1])
            else:
                if len(substr) > len(longest_substr):
                    longest_substr = substr
            j += 1
            substr = s[i:j]

        print(longest_substr)
        return len(longest_substr)


if __name__ == "__main__":
    print(Solution().lengthOfLongestSubstring("abcdeabdceaebcad"))
    print(Solution().lengthOfLongestSubstring("abcabcbb"))
    print(Solution().lengthOfLongestSubstring("pwwkew"))
    print(Solution().lengthOfLongestSubstring("aaaa"))
    print(Solution().lengthOfLongestSubstring("abcdefg"))
    print(Solution().lengthOfLongestSubstring("abababa"))
    print(Solution().lengthOfLongestSubstring("a"))
    print(Solution().lengthOfLongestSubstring(""))
    print(Solution().lengthOfLongestSubstring(None))
    
