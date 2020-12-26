from common import *


class Solution:
    def averageWaitingTime(self, customers: List[List[int]]) -> float:
        cur_time = customers[0][0]
        tot_wait = 0
        for arr, spent in customers:
            cur_time = max(cur_time, arr)
            wait = cur_time - arr + spent
            tot_wait += wait
            cur_time += spent
        return tot_wait / len(customers)