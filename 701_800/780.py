class Solution:
    def reachingPoints(self, sx: int, sy: int, tx: int, ty: int) -> bool:
        while sx < tx and sy < ty:
            if (sx, sy) == (tx, ty):
                return True
            if tx < ty:
                ty %= tx
            else:
                tx %= ty
        if sx == tx:
            return ty >= sy and (ty - sy) % sx == 0
        if sy == ty:
            return tx >= sx and (tx - sx) % sy == 0
        return False
