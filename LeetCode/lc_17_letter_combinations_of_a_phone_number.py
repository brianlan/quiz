from typing import List


class Solution:
    m = {
        "2": ("a", "b", "c"),
        "3": ("d", "e", "f"),
        "4": ("g", "h", "i"),
        "5": ("j", "k", "l"),
        "6": ("m", "n", "o"),
        "7": ("p", "q", "r", "s"),
        "8": ("t", "u", "v"),
        "9": ("w", "x", "y", "z"),
    }

    def letterCombinations(self, digits: str) -> List[str]:
        if len(digits) == 0:
            return []
        combinations = self.m[digits[0]]
        for s in digits[1:]:
            extended_combinations = []
            for l in self.m[s]:
                extended_combinations.extend([seq + l for seq in combinations])
            combinations = extended_combinations
        return combinations


class Solution2:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return list()
        
        phoneMap = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz",
        }

        def backtrack(index: int):
            if index == len(digits):
                combinations.append("".join(combination))
            else:
                digit = digits[index]
                for letter in phoneMap[digit]:
                    combination.append(letter)
                    print(combination)
                    backtrack(index + 1)
                    combination.pop()
                    print(combination)

        combination = list()
        combinations = list()
        backtrack(0)
        return combinations


if __name__ == "__main__":
    print(s:=Solution2().letterCombinations("23"), len(s))
    # print(s:=Solution().letterCombinations("497"), len(s))
