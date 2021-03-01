from collections import Counter


class Solution:
    def isNStraightHand(self, hand: List[int], W: int) -> bool:
        if len(hand) % W != 0:
            return False
        cards = sorted([k, v] for k, v in Counter(hand).items())
        for i, (card, count) in enumerate(cards):
            if count == 0:
                continue
            for j in range(1, W):
                if i + j >= len(cards) or cards[i + j][0] != card + j or cards[i + j][1] < count:
                    return False
                cards[i + j][1] -= count
        return True
