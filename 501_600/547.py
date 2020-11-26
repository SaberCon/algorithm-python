class Solution:
    def findCircleNum(self, M: [[int]]) -> int:
        circles = [i for i in range(len(M))]

        def find_root(n):
            level = 0
            while circles[n] != n:
                n = circles[n]
                level += 1
            return n, level

        for i in range(0, len(M)):
            for j in range(i + 1, len(M)):
                if M[i][j]:
                    i_root, i_level = find_root(i)
                    j_root, j_level = find_root(j)
                    if i_level > j_level:
                        circles[i_root] = j_root
                    else:
                        circles[j_root] = i_root
        for i in range(len(circles)):
            circles[i] = find_root(i)[0]
        return len(set(circles))

Solution().findCircleNum([[1,1,0],[1,1,0],[0,0,1]])
