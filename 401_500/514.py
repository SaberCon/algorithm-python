class Solution:
    def findRotateSteps(self, ring: str, key: str) -> int:
        code_pos = {}
        for i, code in enumerate(ring):
            code_pos.setdefault(code, [])
            code_pos[code].append(i)

        cache = {}

        def find_steps(curr, key_index):
            if (curr, key_index) in cache:
                return cache[curr, key_index]
            if key_index == len(key):
                return 0
            ans = 100000
            for pos in code_pos[key[key_index]]:
                ans = min(ans, min(abs(pos - curr), len(ring) - abs(pos - curr)) + 1 + find_steps(pos, key_index + 1))
            cache[curr, key_index] = ans
            return ans

        return find_steps(0, 0)
