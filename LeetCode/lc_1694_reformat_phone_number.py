from common import *


class Solution:
    def reformatNumber(self, number: str) -> str:
        clean_nunmbers = number.replace("-", "").replace(" ", "")
        n = len(clean_nunmbers)
        if n <= 3:
            return clean_nunmbers
        i = 0
        final_numbers = []
        while i < n - 4:
            final_numbers.append(clean_nunmbers[i:i+3])
            i += 3
        if len(clean_nunmbers[i:]) == 4:
            final_numbers.append(clean_nunmbers[i:i+2])
            final_numbers.append(clean_nunmbers[i+2:])
        else:
            final_numbers.append(clean_nunmbers[i:])
        return "-".join(final_numbers)


if __name__ == "__main__":
    number = "--17-5 229 35-39475 "
    number = "1-23-45 6"
    number = "123 4-567"
    number = "123 4-5678"
    number = "12"

    logger.info(Solution().reformatNumber(number))