from collections import deque, Counter
from typing import List


class Solution:
    def watchedVideosByFriends(self, watchedVideos: List[List[str]], friends: List[List[int]], id: int, level: int) -> List[str]:
        seen = {id}
        queue = deque([(id, 0)])
        count = Counter()
        while queue:
            i, l = queue.popleft()
            if l < level:
                for j in friends[i]:
                    if j not in seen:
                        seen.add(j)
                        queue.append((j, l + 1))
            else:
                count.update(watchedVideos[i])
        return sorted(count.keys(), key=lambda v: (count[v], v))
