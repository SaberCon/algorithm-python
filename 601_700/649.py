class Solution:
    def predictPartyVictory(self, senate: str) -> str:
        senators = [s for s in senate]
        r_banned = d_banned = 0
        while True:
            for i, s in enumerate(senators):
                if s == 'R':
                    if r_banned:
                        senators[i] = 'X'
                        r_banned -= 1
                    else:
                        d_banned += 1
                if s == 'D':
                    if d_banned:
                        senators[i] = 'X'
                        d_banned -= 1
                    else:
                        r_banned += 1
            if all(s == 'R' or s == 'X' for s in senators):
                return 'Radiant'
            if all(s == 'D' or s == 'X' for s in senators):
                return 'Dire'
