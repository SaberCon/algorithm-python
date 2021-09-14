import heapq


class Solution:
    def reachableNodes(self, edges: List[List[int]], maxMoves: int, n: int) -> int:
        connection = [[] for _ in range(n)]
        for n1, n2, cnt in edges:
            connection[n1].append((n2, cnt))
            connection[n2].append((n1, cnt))
        visited = {}
        ans = 0
        queue = [(-maxMoves - 1, 0)]
        while queue:
            moves, i = heapq.heappop(queue)
            if i in visited:
                continue
            moves = -moves - 1
            ans += 1
            visited[i] = {}
            for j, cnt in connection[i]:
                if j in visited:
                    ans += min(moves, cnt - visited[j][i])
                elif moves > cnt:
                    ans += cnt
                    visited[i][j] = cnt
                    heapq.heappush(queue, (cnt - moves, j))
                else:
                    ans += moves
                    visited[i][j] = moves
        return ans
