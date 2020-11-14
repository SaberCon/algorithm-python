class Solution:
    def magicalString(self, n: int) -> int:
        S = []
        curr_index = 0
        curr_val = True
        while len(S) < n:
            S.append(curr_val)
            if not S[curr_index]:
                S.append(curr_val)
            curr_index += 1
            curr_val = not curr_val
        if len(S) > n:
            S.pop()
        return sum(S)
