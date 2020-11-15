class Solution:
    def getMaxRepetitions(self, s1: str, n1: int, s2: str, n2: int) -> int:
        if n1 == 0:
            return 0
        s1cnt, index, s2cnt = 0, 0, 0
        recall = {}
        while True:
            s1cnt += 1
            for ch in s1:
                if ch == s2[index]:
                    index += 1
                    if index == len(s2):
                        s2cnt += 1
                        index = 0
            if s1cnt == n1:
                return s2cnt // n2
            if index in recall:
                break
            recall[index] = (s1cnt, s2cnt)
        s1cnt_prime, s2cnt_prime = recall[index]
        ans = s2cnt_prime + (n1 - s1cnt_prime) // (s1cnt - s1cnt_prime) * (s2cnt - s2cnt_prime)
        for _ in range((n1 - s1cnt_prime) % (s1cnt - s1cnt_prime)):
            for ch in s1:
                if ch == s2[index]:
                    index += 1
                    if index == len(s2):
                        ans += 1
                        index = 0
        return ans // n2
