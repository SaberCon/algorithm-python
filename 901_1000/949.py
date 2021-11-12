class Solution:
    def largestTimeFromDigits(self, arr: List[int]) -> str:
        arr.sort(reverse=True)
        for i1 in range(4):
            for i2 in range(4):
                if i1 == i2:
                    continue
                for i3 in range(4):
                    if i1 == i3 or i2 == i3:
                        continue
                    i4 = 6 - i1 - i2 - i3
                    h, m = arr[i1] * 10 + arr[i2], arr[i3] * 10 + arr[i4]
                    if h >= 24 or m >= 60:
                        continue
                    return "{:02}:{:02}".format(h, m)
        return ''
