class Solution:
    def oddEvenJumps(self, arr: List[int]) -> int:
        N = len(arr)

        def next_jumps(indices):
            jumps = [None] * len(indices)
            stack = []
            for i in indices:
                while stack and stack[-1] < i:
                    jumps[stack.pop()] = i
                stack.append(i)
            return jumps

        odd_next_jumps = next_jumps(sorted(range(N), key=lambda i: arr[i]))
        even_next_jumps = next_jumps(sorted(range(N), key=lambda i: -arr[i]))
        odd_good = [False] * (N - 1) + [True]
        even_good = [False] * (N - 1) + [True]
        for i in range(N - 2, -1, -1):
            if odd_next_jumps[i] and even_good[odd_next_jumps[i]]:
                odd_good[i] = True
            if even_next_jumps[i] and odd_good[even_next_jumps[i]]:
                even_good[i] = True
        return sum(odd_good)
