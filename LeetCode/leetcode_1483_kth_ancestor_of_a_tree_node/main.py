from typing import List
from functools import lru_cache
from collections import deque


class TreeAncestor:
    def __init__(self, n: int, parent: List[int]):
        self.parent = parent

    def getKthAncestor(self, node: int, k: int) -> int:
        cur_node = node
        for _ in range(k):
            if cur_node == -1:
                break
            cur_node = self.parent[cur_node]
        return cur_node


class TreeAncestor2:
    def __init__(self, n: int, parent: List[int]):
        self.parent = parent
    
    @lru_cache(maxsize=None)
    def getKthAncestor(self, node: int, k: int) -> int:
        if node == -1:
            return -1
        if k == 1:
            return self.parent[node]
        return self.getKthAncestor(self.parent[node], k - 1)


class TreeAncestor3:
    def __init__(self, n: int, parent: List[int]):
        self.parent = parent
        self.cache = {}

    def write_cache(self, visited_nodes, cur_node):
        for pos, v in enumerate(visited_nodes):
            if pos > 0:
                self.cache[(v, pos + 1)] = cur_node

    def getKthAncestor(self, node: int, k: int) -> int:
        visited_nodes = deque()
        cur_node = node
        for _, cur_k in enumerate(range(k, 0, -1)):
            print(cur_node, cur_k)
            visited_nodes.appendleft(cur_node)
            if cur_node == -1:
                return cur_node
            if cur_k == 1:
                self.write_cache(visited_nodes, self.parent[cur_node])
                return self.parent[cur_node]
            if (cur_node, cur_k) in self.cache:
                print(f"uses cache ({cur_node}, {cur_k})")
                return self.cache[(cur_node, cur_k)]
            
            cur_node = self.parent[cur_node]
            self.write_cache(visited_nodes, cur_node)
            
        return cur_node


class TreeAncestor4:
    def __init__(self, n: int, parent: List[int]):
        self.cols = 20      # log(50000) < 20

        self.dp = [[-1] * self.cols for _ in range(n)]
        for i in range(n):
            self.dp[i][0] = parent[i]
        # 动态规划设置祖先, dp[node][j] 表示 node 往前推第 2^j 个祖先
        for j in range(1, self.cols):
            for i in range(n):
                if self.dp[i][j-1] != -1:
                    self.dp[i][j] = self.dp[self.dp[i][j-1]][j-1]

    def getKthAncestor(self, node: int, k: int) -> int:
        for i in range(self.cols - 1, -1, -1):
            if k & (1 << i):
                node = self.dp[node][i]
                if node == -1:
                    break
        return node


if __name__ == "__main__":
    # ta = TreeAncestor3(15, [-1, 0, 0, 1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 6])
    # print(ta.getKthAncestor(14, 3))
    # print(ta.cache)
    # print(ta.getKthAncestor(13, 3))
    # print(ta.cache)
    ta = TreeAncestor4(50000, list(range(-1, 49999)))
    print(ta.getKthAncestor(43495, 41615))
    print(ta.getKthAncestor(49488, 46898))
    print(ta.getKthAncestor(44108, 44236))
    print(ta.getKthAncestor(42483, 49825))
    # print(ta.getKthAncestor(5, 2))
    # print(ta.getKthAncestor(6, 3))
