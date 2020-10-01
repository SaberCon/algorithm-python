class Solution:
    def readBinaryWatch(self, num: int) -> List[str]:
        result = []
        hour = [1, 2, 4, 8]
        minute = [1, 2, 4, 8, 16, 32]
        status = [0 for _ in range(len(hour) + len(minute))]

        def backtrace(remain, index):
            if remain == 0:
                h = sum([i * j for i, j in zip(hour, status[:len(hour)])])
                m = sum([i * j for i, j in zip(minute, status[len(hour):])])
                if h < 12 and m < 60:
                    result.append("%d:%02d" % (h, m))
                return
            for i in range(index, len(status)):
                status[i] = 1
                backtrace(remain - 1, i + 1)
                status[i] = 0

        backtrace(num, 0)
        return result
