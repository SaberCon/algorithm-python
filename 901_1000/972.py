class Solution:
    def isRationalEqual(self, s: str, t: str) -> bool:
        def standardize(number):
            parts = number.split('.')
            integer, decimal = int(parts[0]), (parts[1] if len(parts) > 1 and parts[1] else '0')
            parts = decimal[:-1].split('(') if '(' in decimal else [decimal, '0']
            decimal = parts[0] + parts[1] * 8
            non_repeat = int(decimal[:4])
            repeat_size = 1 if len(set(parts[1])) == 1 else len(parts[1])
            if repeat_size == 2:
                repeat_size = 4
            repeat = int(decimal[4:4 + repeat_size])
            if repeat == 9:
                repeat = 0
                non_repeat += 1
                if non_repeat == 10000:
                    non_repeat = 0
                    integer += 1
            return integer, non_repeat, repeat

        return standardize(s) == standardize(t)
