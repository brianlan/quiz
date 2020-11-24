from typing import List


class Solution:
    def __init__(self) -> None:
        self.cache = None

    def gen(self, x, y):
        if x == 0:
            return [")" * y]
        if y == 0:
            return ["(" * x]
        if self.cache.get((x, y)) is None:
            left = ["(" + s for s in self.gen(x - 1, y)]
            right = [")" + s for s in self.gen(x, y - 1)]
            # print(f"[{x}, {y}] set cache: {self.cache.get((x, y))} = {left} + {right}")
            self.cache[(x, y)] = left + right
        print(f"[{x}, {y}] {self.cache[(x, y)]}")
        return self.cache[(x, y)]

    @staticmethod
    def remove_invalid(candidates):
        final = []
        for s in candidates:
            stack = []
            try:
                for i in range(len(s)):
                    if s[i] == '(':
                        stack.append(1)
                    else:
                        stack.pop()
            except IndexError:
                pass
            else:
                final.append(s)
        return final

    def generateParenthesis(self, n: int) -> List[str]:
        self.cache = {}
        candidates = self.gen(n, n)
        final = self.remove_invalid(candidates)
        return final


if __name__ == "__main__":
    print(Solution().generateParenthesis(3))