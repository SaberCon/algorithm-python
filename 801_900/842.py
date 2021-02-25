class Solution:
    def splitIntoFibonacci(self, S: str) -> List[int]:
        for i in range(min(len(S) * 2 // 3, 20), 1, -1):
            for j in range(1, min(i, 10)):
                if (S[0] == '0' and j != 1) or (S[j] == '0' and i != j + 1):
                    continue
                ans = [int(S[:j]), int(S[j:i])]
                curr = i
                while curr != len(S):
                    if ans[-1] + ans[-2] > 2 ** 31 - 1:
                        break
                    n = str(ans[-1] + ans[-2])
                    if not S.startswith(n, curr):
                        break
                    ans.append(int(n))
                    curr += len(n)
                else:
                    return ans
        return []
