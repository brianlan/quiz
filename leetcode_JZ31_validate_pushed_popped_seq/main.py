from typing import List

class Solution:
    def validateStackSequences(self, pushed: List[int], popped: List[int]) -> bool:
        """WRONG ALGORITHM!!! DON'T use it. """
        if len(pushed) == 0 or len(popped) == 0:
            return True
        while len(popped) > 0:
            i = popped[0]
            push_pos = pushed.index(i)
            push_to_valid = pushed[:push_pos]
            pop_pos = 1
            for j in reversed(push_to_valid):
                try:
                    delta = popped[pop_pos:].index(j)
                except ValueError:
                    return False
                pushed.remove(j)
                popped.remove(j)
                pop_pos += delta
            pushed.remove(i)
            popped.remove(i)
        return True


if __name__ == "__main__":
    # print(Solution().validateStackSequences([1,2,3,4,5,6,7,8,9], [4,3,2,1,5,6,8,9,7]))
    # print(Solution().validateStackSequences([1,2,3,4,5,6,7,8,9], [2,3,5,4,8,7,9,6,1]))
    print(Solution().validateStackSequences([8,2,1,4,7,9,0,3,5,6], [1,2,7,3,6,4,0,9,5,8]))

    
