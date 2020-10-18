class Solution:
    def strongPasswordChecker(self, s: str) -> int:
        # 计算保持三种字符所需的替换或插入次数
        min_r_or_i = 3 - any(c.islower() for c in s) - any(c.isupper() for c in s) - any(c.isdigit() for c in s)
        # 长度小于 6 时重复字串不是主导因素
        if len(s) < 6:
            return max(6 - len(s), min_r_or_i)
        # 计算处理重复子串的最小次数, 替换优于插入优于删除
        count = 0
        repeat_count = {1: 0, 2: 0, 3: 0}
        for c, last_c in zip(s + '.', '.' + s):
            if c != last_c:
                if count > 2:
                    repeat = count - 2
                    for i in [3, 2, 1]:
                        repeat_count[i] += repeat // i
                        repeat %= i
                count = 0
            count += 1
        # 长度小于等于 20 时都使用替换
        if len(s) <= 20:
            return max(sum(repeat_count.values()), min_r_or_i)
        # 长度大于 20, 考虑加入删除操作
        min_remove = len(s) - 20
        for i in range(1, 4):
            if min_remove > repeat_count[i] * i:
                min_remove -= repeat_count[i] * i
                repeat_count[i] = repeat_count[i] * i
            else:
                repeat_count[i] = (repeat_count[i] * i - min_remove + i - 1) // i + min_remove
                break
        return max(sum(repeat_count.values()), len(s) - 20 + min_r_or_i)
