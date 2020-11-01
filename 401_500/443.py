class Solution:
    def compress(self, chars: List[str]) -> int:
        index = 0
        prev = chars[0]
        count = 0
        chars.append('end')
        for c in chars:
            if prev == c:
                count += 1
            else:
                chars[index] = prev
                index += 1
                if count != 1:
                    for n in str(count):
                        chars[index] = n
                        index += 1
                count = 1
                prev = c
        return index
