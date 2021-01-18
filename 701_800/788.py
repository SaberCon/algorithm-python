class Solution:
    def rotatedDigits(self, N: int) -> int:
        valid = [1, 2, 3, 3, 3, 4, 5, 5, 6, 7]
        good = [0, 0, 1, 1, 1, 2, 3, 3, 3, 4]

        def find_good_count(digit, size):
            if size == 0:
                return good[digit]
            if digit == 0:
                return 0
            return valid[digit - 1] * (valid[-1] ** size) - (valid[digit - 1] - good[digit - 1]) * (
                    (valid[-1] - good[-1]) ** size)

        def find_valid_count(digit, size):
            if size == 0:
                return valid[digit]
            if digit == 0:
                return 0
            return valid[digit - 1] * (valid[-1] ** size)

        ans = 0
        s = str(N)
        is_good = False
        for i, d in enumerate(s):
            d = int(d)
            ans += find_valid_count(d, len(s) - i - 1) if is_good else find_good_count(d, len(s) - i - 1)
            if d in (2, 5, 6, 9):
                is_good = True
            if d in (3, 4, 7):
                break
        return ans
