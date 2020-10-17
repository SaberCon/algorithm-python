class Solution:
    def strongPasswordChecker(self, s: str) -> int:
        if not s:
            return 6
        min_remove = max(0, len(s) - 20)
        min_insert = max(0, 6 - len(s))
        min_move = min_remove + max(min_insert, 3 - any(c.islower() for c in s) - any(c.isupper() for c in s) - any(
            c.isdigit() for c in s))

        last_c = s[0]
        count = 1
        repeat_count = {1: 0, 2: 0, 3: 0}
        for c in (s + '.')[1:]:
            if c == last_c:
                count += 1
            else:
                if count > 2:
                    count -= 2
                    repeat_count[3] += count // 3
                    repeat_count[2] += (count % 3) // 2
                    repeat_count[1] += (count % 3) % 2
                last_c = c
                count = 1

        if min_remove > repeat_count[1]:
            min_remove -= repeat_count[1]
            if min_remove > repeat_count[2] * 2:
                min_remove -= repeat_count[2] * 2
                repeat_count[2] = repeat_count[2] * 2
                if min_remove < repeat_count[3] * 3:
                    repeat_count[3] = min_remove + (repeat_count[3] * 3 - min_remove + 2) // 3
            else:
                repeat_count[2] = min_remove + (repeat_count[2] * 2 - min_remove + 1) // 2

        if min_insert > repeat_count[1] + repeat_count[2]:
            min_insert -= repeat_count[1] + repeat_count[2]
            if min_insert < repeat_count[3] * 3:
                repeat_count[3] = min_insert + (repeat_count[3] * 3 - min_insert * 2 + 2) // 3

        move_count = sum(repeat_count.values())
        return max(move_count, min_move)


print(Solution().strongPasswordChecker("1010101010aaaB10101010"))
