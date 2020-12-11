from typing import List
import numpy as np
from loguru import logger

class Solution:
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
    """Cut candidates during first children layer search of each sub-tree's root.
    The idea is that since the combination doesn't care about order and each 
    child branch created by picking a candidate number actually means the rest 
    part of combination contains the picked number.
    """
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        logger.debug(candidates)
        logger.debug(target)
        self.combinations = set()
        self.sorted_candidates = sorted(candidates)
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
            if not hope:
                break
        return True


if __name__ == "__main__":
    # candidates = (np.random.choice(np.arange(20), size=10, replace=False) + 1).tolist()
    # target = np.random.randint(50) + 1
    candidates = [15, 20, 5, 6, 7, 1, 14, 4, 3, 16]
    target = 31
    print(Solution2().combinationSum(candidates, target))
