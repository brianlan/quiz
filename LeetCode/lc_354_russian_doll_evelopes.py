import math
from typing import List

import numpy as np
from loguru import logger


# class Envelope:
#     def __init__(self, w, h) -> None:
#         self.w, self.h = w, h

#     def __lt__(self, __o: object) -> bool:
#         return self.w < __o.w or (self.w == __o.w and self.h < __o.h)

#     def __gt__(self, __o: object) -> bool:
#         return self.w > __o.w or (self.w == __o.w and self.h > __o.h)

#     def __eq__(self, __o: object) -> bool:
#         return self.w == __o.w or self.h == __o.h

#     def __le__(self, __o: object) -> bool:
#         return self < __o or self == __o

#     def __ge__(self, __o: object) -> bool:
#         return self > __o or self == __o

#     def __repr__(self) -> str:
#         return f"[{self.w}, {self.h}]"


class Solution:
    def maxEnvelopes(self, envelopes: List[List[int]]) -> int:
        sorted_envelopes = sorted(envelopes, key=lambda x: (x[0], x[1]))
        # logger.debug(sorted_envelopes)
        dp = [1] * len(envelopes)
        for i in range(1, len(envelopes)):
            tmp = [
                dp[j] + 1 for j in range(i) if sorted_envelopes[j][0] < sorted_envelopes[i][0] and sorted_envelopes[j][1] < sorted_envelopes[i][1]
            ]
            if tmp:
                dp[i] = max(tmp)
        # logger.debug(max(dp))
        return max(dp)


if __name__ == "__main__":
    # assert Solution().maxEnvelopes([[10, 17], [10, 19], [16, 2], [19, 18], [5, 6]]) == 3
    # assert Solution().maxEnvelopes([[5, 4], [6, 4], [6, 7], [2, 3]]) == 3
    # assert Solution().maxEnvelopes([[1, 1], [1, 1], [1, 1]]) == 1
    assert Solution().maxEnvelopes([[i, i] for i in range(1, 10001)]) == 10000
