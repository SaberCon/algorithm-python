from typing import List


class Solution:
    def destCity(self, paths: List[List[str]]) -> str:
        return ({t for f, t in paths} - {f for f, t in paths}).pop()
