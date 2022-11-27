from typing import List

from loguru import logger


class Solution:
    def number_of_connected_subgraph(self, n: int, edges: List[List[int]]) -> int:
        subgraphs = []
        for e in edges:
            for g in subgraphs:
                if e[0] in g or e[1] in g:
                    g.add(e[0])
                    g.add(e[1])
                    break
            else:
                subgraphs.append(set(e))
        single_pts = n - sum([len(i) for i in subgraphs])
        logger.debug(subgraphs)
        return len(subgraphs) + single_pts


if __name__ == "__main__":
    assert Solution().number_of_connected_subgraph(5, [[0, 1], [1, 2], [3, 4]]) == 2
    assert Solution().number_of_connected_subgraph(14, [[0, 1], [0, 2], [0, 12], [11, 10], [3, 9], [6, 5], [5, 4], [4, 7], [5, 8]]) == 5
