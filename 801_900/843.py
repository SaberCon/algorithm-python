class Master:
    def guess(self, word: str) -> int:
        pass


class Solution:
    def findSecretWord(self, wordlist: List[str], master: 'Master') -> None:
        size = len(wordlist)
        possible = set(range(size))
        matches = [[set() for _ in range(6)] for _ in range(size)]
        for i, w1 in enumerate(wordlist):
            for j, w2 in enumerate(wordlist):
                if i == j:
                    continue
                matches[i][sum(1 for c1, c2 in zip(w1, w2) if c1 == c2)].add(j)
        while True:
            curr = min(possible, key=lambda i: max(len(s & possible) for s in matches[i]))
            res = master.guess(wordlist[curr])
            if res == 6:
                return
            possible &= matches[curr][res]
