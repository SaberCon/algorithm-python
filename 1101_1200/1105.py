class Solution:
    def minHeightShelves(self, books: List[List[int]], shelfWidth: int) -> int:
        dp = [100000000] * (len(books) + 1)
        dp[0] = 0
        for i, (thickness, height) in enumerate(books):
            total_thickness = thickness
            max_height = height
            j = i
            while total_thickness <= shelfWidth and j >= 0:
                dp[i + 1] = min(dp[i + 1], dp[j] + max_height)
                total_thickness += books[j - 1][0]
                max_height = max(max_height, books[j - 1][1])
                j -= 1
        return dp[-1]
