from common import *
from collections import Counter

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        # logger.debug(f'\n"{s}"\n"{t}"')
        n = len(s)
        target_cnt = defaultdict(int)
        _ = [target_cnt.update({c: target_cnt[c]+1}) for c in t]
        current_cnt = {k: 0 for k, _ in target_cnt.items()}
        start, end = 0, 0
        _min_window = ""
        while end < n:
            if (l:=s[end]) in current_cnt:
                current_cnt[l] += 1
            if all([v >= target_cnt[k] for k, v in current_cnt.items()]):
                f = s[start]
                while (f:=s[start]) not in target_cnt or current_cnt[f] - target_cnt[f] > 0:
                    if f in current_cnt:
                        current_cnt[f] -= 1
                    start += 1
                if len(w:=s[start:end+1]) < len(_min_window) or _min_window == "":
                    _min_window = w
            # logger.debug(f"{s[start:end+1]}")
            end += 1
        return _min_window


if __name__ == "__main__":
    # s = "ADOBECODEBANCX"
    # t = "ABCA"
    # s = "a"
    # t = "a"
    # s = "CFBAEEEDECED"
    # t = "ECECD"
    s = "cabwefgewcwaefgcf"
    t = "cae"
    # s = "".join([chr(65 + i) for i in np.random.randint(10, size=50)])
    # t = "".join([chr(65 + j) for j in np.random.randint(7, size=12)])
    logger.info(Solution().minWindow(s, t))
