from typing import List

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        common_prefix = []
        for elements in zip(*strs):
            if len(set(elements)) == 1:
                common_prefix.append(elements[0])
            else:
                break
        return ''.join(common_prefix)
