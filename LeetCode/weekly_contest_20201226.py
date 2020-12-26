from common import *
import math
from data_structures.queue import MinMaxQueue


class Solution1:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        for san in sandwiches:
            try:
                first_match = students.index(san)
                students = students[first_match + 1 :] + students[:first_match]
            except ValueError:
                return len(students)
        return 0


class Solution2:
    def averageWaitingTime(self, customers: List[List[int]]) -> float:
        cur_time = customers[0][0]
        tot_wait = 0
        for arr, spent in customers:
            cur_time = max(cur_time, arr)
            wait = cur_time - arr + spent
            tot_wait += wait
            cur_time += spent
        return tot_wait / len(customers)


class Solution3:
    def minMoves(self, nums: List[int], k: int) -> int:
        if len(nums) == 1:
            return 0
        cost = []
        i = 0
        while nums[i] == 0:
            i += 1
        j = i + 1
        while j < len(nums):
            if nums[j] == 1:
                cost.append(j - i - 1)
                i = j
            j += 1
        if len(cost) == 0:
            return 0
        window_len = k - 1
        min_moves, min_move_range = math.inf, None
        cumsum = [0] + list(accumulate(cost))
        for i in range(window_len, len(cumsum)):
            range_sum = cumsum[i] - cumsum[i - window_len]
            if range_sum < min_moves:
                min_moves = range_sum
                min_move_range = i - window_len, i
        order = (len(min_move_range) - 1) // 2 - 1
        logger.debug(min_move_range)
        return min_moves


if __name__ == "__main__":
    # nums = [1, 1, 0 ,0, 1, 0, 0, 1, 0, 0, 1, 1, 0, 0, 0, 1]
    # nums, k = [1, 0, 0, 1, 0, 1], 2
    # nums, k = [1, 0, 0, 0, 0, 0, 1, 1], 3
    # nums, k = [1, 1, 0, 1], 2
    nums, k = [1, 0, 0, 1, 0, 1, 1, 1, 0, 1, 1], 7
    logger.info(Solution3().minMoves(nums, k))
    # customers = [[1, 2], [2, 5], [4, 3]]
    # # customers = [[5, 2], [5, 4], [10, 3], [20, 1]]
    # logger.info(Solution2().averageWaitingTime(customers))
    # students = [1, 1, 1, 0, 0, 1]
    # sandwiches = [1, 0, 0, 0, 1, 1]
    # students = [1, 1, 0, 0]
    # sandwiches = [0, 1, 0, 1]
    # students = np.random.randint(2, size=10).tolist()
    # sandwiches = np.random.randint(2, size=10).tolist()
    # logger.debug(students)
    # logger.debug(sandwiches)
    # logger.info(Solution1().countStudents(students, sandwiches))
