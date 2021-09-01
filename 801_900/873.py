class Solution:
    def lenLongestFibSubseq(self, arr: List[int]) -> int:
        seq_count = {}
        for i in range(1, len(arr)):
            for j in range(i):
                if (arr[j], arr[i] - arr[j]) in seq_count:
                    seq_count[(arr[i] - arr[j], arr[i])] = max(3, seq_count[(arr[j], arr[i] - arr[j])] + 1)
                    del seq_count[(arr[j], arr[i] - arr[j])]
                if (arr[j], arr[i]) not in seq_count:
                    seq_count[(arr[j], arr[i])] = 0
        return max(seq_count.values())
