from common import *


class Solution:
    def fourSumCount(self, A: List[int], B: List[int], C: List[int], D: List[int]) -> int:
        ab, cd = defaultdict(int), defaultdict(int)
        for a in A:
            for b in B:
                ab[a + b] += 1
        for c in C:
            for d in D:
                cd[-c - d] += 1
        ans = 0
        for k, v in ab.items():
            ans += cd.get(k, 0) * v
        return ans


class Solution2:
    def fourSumCount(self, A: List[int], B: List[int], C: List[int], D: List[int]) -> int:
        dic = Counter([a + b for a in A for b in B])
        return sum([dic.get(-c - d, 0) for c in C for d in D])


if __name__ == "__main__":
    A = (np.random.randint(1000, size=500) - 500).tolist()
    B = (np.random.randint(1000, size=500) - 500).tolist()
    C = (np.random.randint(1000, size=500) - 500).tolist()
    D = (np.random.randint(1000, size=500) - 500).tolist()
    # A = (np.random.randint(20, size=10) - 10).tolist()
    # B = (np.random.randint(20, size=10) - 10).tolist()
    # C = (np.random.randint(20, size=10) - 10).tolist()
    # D = (np.random.randint(20, size=10) - 10).tolist()
    # logger.debug(A)
    # logger.debug(B)
    # logger.debug(C)
    # logger.debug(D)
    logger.info(Solution().fourSumCount(A, B, C, D))
    logger.info(Solution2().fourSumCount(A, B, C, D))
