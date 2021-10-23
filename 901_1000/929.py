class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:
        return len({e.split('@')[0].split('+')[0].replace('.', '') + '@' + e.split('@')[1] for e in emails})