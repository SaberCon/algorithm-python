from collections import Counter


class Solution:
    def originalDigits(self, s: str) -> str:
        # zero one two three four five six seven eight nine
        counter = Counter(s)
        ans = ''

        ans += '0' * counter['z']
        counter.subtract('zero' * counter['z'])
        ans += '2' * counter['w']
        counter.subtract('two' * counter['w'])
        ans += '4' * counter['u']
        counter.subtract('four' * counter['u'])
        ans += '1' * counter['o']
        counter.subtract('one' * counter['o'])
        ans += '3' * counter['r']
        counter.subtract('three' * counter['r'])
        ans += '5' * counter['f']
        counter.subtract('five' * counter['f'])
        ans += '6' * counter['x']
        counter.subtract('six' * counter['x'])
        ans += '7' * counter['s']
        counter.subtract('seven' * counter['s'])
        ans += '8' * counter['h']
        counter.subtract('eight' * counter['h'])
        ans += '9' * counter['i']
        counter.subtract('nine' * counter['i'])

        return ''.join(sorted(ans))
