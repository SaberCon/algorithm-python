from heapq import *


class Solution:
    def medianSlidingWindow(self, nums: [int], k: int) -> [float]:
        if not nums:
            return []
        max_heap, min_heap, ans = [], [], []
        removed = {num: 0 for num in nums}
        is_min_next = True
        for i in range(0, len(nums)):
            if not min_heap or nums[i] >= min_heap[0]:
                heappush(min_heap, nums[i])
                if not is_min_next:
                    heappush(max_heap, -heappop(min_heap))
            else:
                heappush(max_heap, -nums[i])
                if is_min_next:
                    heappush(min_heap, -heappop(max_heap))
            is_min_next = not is_min_next
            if i >= k:
                removed[nums[i - k]] += 1
                if nums[i - k] >= min_heap[0]:
                    if is_min_next:
                        heappush(min_heap, -heappop(max_heap))
                    else:
                        is_min_next = True
                else:
                    if is_min_next:
                        is_min_next = False
                    else:
                        heappush(max_heap, -heappop(min_heap))
                while removed[min_heap[0]]:
                    removed[min_heap[0]] -= 1
                    heappop(min_heap)
                while max_heap and removed[-max_heap[0]]:
                    removed[-max_heap[0]] -= 1
                    heappop(max_heap)
            if i + 1 >= k:
                ans.append(min_heap[0] if k % 2 else (min_heap[0] - max_heap[0]) / 2)
        return ans
