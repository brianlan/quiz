from common import *


class Solution:
    def countPairs(self, deliciousness: List[int]) -> int:
        max_power = 21
        powers = [2 ** p for p in range(max_power + 1)]
        cache = defaultdict(int)
        cnt = 0
        for d in deliciousness:
            cnt += cache[d]
            for p in powers:
                cache[p - d] += 1
        cnt %= 1000000007
        return cnt


if __name__ == "__main__":
    deliciousness = np.random.randint(20, size=10).tolist()
    # deliciousness = [1, 3, 5, 7, 9]
    # deliciousness = [1, 1, 1, 3, 3, 3, 7]
    logger.debug(deliciousness)
    logger.info(Solution().countPairs(deliciousness))
