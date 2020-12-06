import heapq


class Solution:
    def scheduleCourse(self, courses: List[List[int]]) -> int:
        courses.sort(key=lambda c: (c[1], c[0]))
        heap = []
        curr = 0
        for duration, deadline in courses:
            if curr + duration <= deadline:
                curr += duration
                heapq.heappush(heap, -duration)
            elif heap and heap[0] < -duration:
                curr += heapq.heappop(heap) + duration
                heapq.heappush(heap, -duration)
        return len(heap)
