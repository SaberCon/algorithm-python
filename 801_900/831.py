class Solution:
    def maskPII(self, S: str) -> str:
        if '@' in S:
            p1, p2 = S.split('@')
            return p1[0].lower() + '*****' + p1[-1].lower() + '@' + p2.lower()
        else:
            digits = ''.join(filter(lambda s: s.isdigit(), S))
            size = len(digits)
            return ('' if size <= 10 else '+' + '*' * (size - 10) + '-') + '***-***-' + digits[-4:]
