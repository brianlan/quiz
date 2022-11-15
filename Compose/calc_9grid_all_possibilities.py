from typing import List, Tuple


class Solution:
    next_moves = {
        (0, 0): [(0, 2), (1, 2), (2, 0), (2, 1), (2, 2)],
        (0, 1): [(2, 0), (2, 1), (2, 2)],
        (0, 2): [(0, 0), (1, 0), (2, 0), (2, 1), (2, 2)],
        (1, 0): [(0, 2), (1, 2), (2, 2)],
        (1, 2): [(0, 0), (1, 0), (2, 0)],
        (2, 0): [(0, 0), (0, 1), (0, 2), (1, 2), (2, 2)],
        (2, 1): [(0, 0), (0, 1), (0, 2)],
        (2, 2): [(0, 0), (0, 1), (0, 2), (1, 0), (2, 0)],
    }

    def solve(self, start=None, num_key_pts=5) -> List[List[Tuple[int, int]]]:
        pool = []

        def move(cur_state):
            if len(cur_state) == num_key_pts:
                pool.append(cur_state)
                return
            cur_loc = cur_state[-1]
            for next_loc in self.next_moves[cur_loc]:
                if next_loc not in cur_state:
                    move(cur_state + [next_loc])
        
        if start is not None:
            move([start])
        else:
            for start in [(0, 0), (0, 1), (0, 2), (1, 0), (1, 2), (2, 0), (2, 1), (2, 2)]:
                move([start])

        return pool


def visualize_state(state):
    board = [[0] * 3 for _ in range(3)]
    for i, s in enumerate(state):
        board[s[0]][s[1]] = i + 1
    
    def _list2str(l):
        return ''.join([str(i) for i in l])

    return f'{_list2str(board[0])}\n{_list2str(board[1])}\n{_list2str(board[2])}'


if __name__ == "__main__":
    print(len(Solution().solve()))
    # for s in Solution().solve((1, 0)):
    #     print(visualize_state(s))
    #     print('-' * 3)

    # validate
    
