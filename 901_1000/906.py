import math


class Solution:
    def superpalindromesInRange(self, left: str, right: str) -> int:
        left = math.ceil(int(left) ** 0.5)
        right = math.floor(int(right) ** 0.5)
        ans = sum(1 for i in range(1, 4) if left <= i <= right)

        def build_palindrome(half, mid=''):
            return int(half + mid + half[::-1])

        memo = {}

        def build_10(l, m):
            if m < 0:
                return []
            if l == 0:
                return ['']
            if (l, m) not in memo:
                memo[l, m] = ['0' + s for s in build_10(l - 1, m)] + ['1' + s for s in build_10(l - 1, m - 2)]
            return memo[l, m]

        for i in range(max(2, len(str(left))), len(str(right)) + 1):
            sps = []
            if i % 2:
                for j in range(0, 3):
                    sps += [build_palindrome('1' + oz, str(j)) for oz in build_10(i // 2 - 1, 7 - j * j)]
                    sps += [build_palindrome('2' + oz, str(j)) for oz in build_10(i // 2 - 1, 1 - j * j)]
            else:
                sps += [build_palindrome('1' + oz) for oz in build_10(i // 2 - 1, 7)]
                sps += [build_palindrome('2' + oz) for oz in build_10(i // 2 - 1, 1)]

            ans += sum(1 for sp in sps if left <= sp <= right)
        return ans
