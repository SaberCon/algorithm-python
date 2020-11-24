class Solution:
    def countArrangement(self, N: int) -> int:
        cache = {}

        def get_count(curr, used):
            if (curr, used) in cache:
                return cache[curr, used]
            if curr > N:
                return 1
            count = 0
            for i, is_used in enumerate(used):
                if is_used == "1" or ((i + 1) % curr and curr % (i + 1)):
                    continue
                count += get_count(curr + 1, used[:i] + "1" + used[i + 1:])
            cache[curr, used] = count
            return count

        return get_count(1, "0" * N)
