from collections import deque


class Solution:
    def deckRevealedIncreasing(self, deck: List[int]) -> List[int]:
        N = len(deck)
        deck.sort()
        indices = deque(range(N))
        ranks = deque()
        while indices:
            ranks.append(indices.popleft())
            if indices:
                indices.append(indices.popleft())

        ans = [0] * N
        for rank, card in zip(ranks, deck):
            ans[rank] = card
        return ans
