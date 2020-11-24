from functools import lru_cache

class Solution:
    def __init__(self, max_n=2*pow(10, 9)) -> None:
        self.days = [0] * (max_n + 1)
        for i in range(1, max_n + 1):
            if i == 1:
                self.days[i] = 1
            elif i % 2 == 0 and i % 3 != 0:
                self.days[i] = 1 + min(self.days[i - 1], self.days[i // 2])
            elif i % 3 == 0 and i % 2 != 0:
                self.days[i] = 1 + min(self.days[i - 1], self.days[i // 3])
            elif i % 6 == 0:
                self.days[i] = 1 + min(self.days[i - 1], self.days[i // 3], self.days[i // 2])
            else:
                self.days[i] = 1 + self.days[i - 1]

    def minDays(self, n: int) -> int:
        return self.days[n]


class Solution2:
    @lru_cache(maxsize=None)
    def minDays(self, n: int) -> int:
        if n == 0:
            return 0
        elif n == 1:
            return 1
        elif n % 2 == 0 and n % 3 != 0:
            return 1 + min(self.minDays(n - 1), self.minDays(n // 2))
        elif n % 3 == 0 and n % 2 != 0:
            return 1 + min(self.minDays(n - 1), self.minDays(n // 3))
        elif n % 6 == 0:
            return 1 + min(self.minDays(n - 1), self.minDays(n // 3), self.minDays(n // 2))
        else:
            return 1 + self.minDays(n - 1)


class Solution3:
    @lru_cache(maxsize=None)
    def minDays(self, n: int) -> int:
        if n == 0:
            return 0
        elif n == 1:
            return 1
        return 1 + min(self.minDays(n // 2) + n % 2, self.minDays(n // 3) + n % 3)


if __name__ == "__main__":
    print(Solution3().minDays(10))
    print(Solution3().minDays(16))
    print(Solution3().minDays(32))
    print(Solution3().minDays(56))
