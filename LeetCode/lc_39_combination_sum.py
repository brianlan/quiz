from typing import List
import numpy as np
from loguru import logger

class Solution:
    """因为数据量不大，而且需要输出具体的每一个组合，而不仅是组合的数目，因此可以考虑用DFS + 回溯
    """
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        logger.debug(candidates)
        logger.debug(target)
        self.combinations = set()
        self.sorted_candidates = sorted(candidates)
        self.dfs([], target)
        return [list(c) for c in self.combinations]
    
    def dfs(self, picked_elements, target) -> bool:
        if target == 0:
            self.combinations.add(tuple(sorted(picked_elements)))
            return False
        if target < 0:
            return False
        for c in self.sorted_candidates:
            hope = self.dfs(picked_elements + [c], target - c)
            if not hope:
                break
        return True


class Solution2:
    """在DFS+回溯思想上增加优化：
    由于对candidates进行了排序，而且DFS的过程中，总是尽可能的尝试用当前最小的数字来凑组合。
    如果尝试到组合之和超过了target，那么就会回溯，接下来会选用比当前数字稍大的数字来尝试。
    此时，我们可以限制candidates：排除掉刚才试过的小数字，因为之前已经考虑过该分支中小数字最多
    的那种情况了。例如：candidates: [5, 6, 8, 12], target=18
    按照DFS的流程进行，[5,5,5,5]失败回溯到下一个可能分支[5,5,6]时，不用再尝试[5,5,6,5]这种可能了
    因为组合中的数字是“顺序无关”的，包含3个5的组合之前已经尝试过了，而且用更小的5作为第4个数时
    已经失败了。所以接下来DFS要去尝试的是[5,5,6,6]了。那么如果DFS继续演进的话，接下来会发现这也是
    个不满足target的组合，于是继续回溯到[5,5,8](局部candidates为8,12), 
    而不是[5,5,8](局部candidates为6,8,12)，因为[5,5,6,6]都不成功了，也意味着[5,5,6,8]也不会成功，
    因此[5,5,8,6]也没必要试了
    """
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        logger.debug(candidates)
        logger.debug(target)
        self.combinations = set()
        self.sorted_candidates = sorted(candidates)
        logger.debug(f"\n{self.sorted_candidates}")
        self.dfs([], target)
        return [list(c) for c in self.combinations]
    
    def dfs(self, picked_elements, target, begin=0) -> bool:
        if target == 0:
            self.combinations.add(tuple(sorted(picked_elements)))
            return False
        if target < 0:
            return False
        for i, c in enumerate(self.sorted_candidates[begin:]):
            hope = self.dfs(picked_elements + [c], target - c, begin=begin+i)
            if not hope:  # meaning: the smallest num can not even meet current target
                break
        return True


if __name__ == "__main__":
    # candidates = (np.random.choice(np.arange(20), size=10, replace=False) + 1).tolist()
    # target = np.random.randint(50) + 1
    # candidates = [15, 20, 5, 6, 7, 1, 14, 4, 3, 16]
    # target = 31
    # candidates, target = [2,3,6,7], 7
    candidates, target = [5, 6, 8, 12], 18
    print(Solution2().combinationSum(candidates, target))
