class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        uf = [i for i in range(len(accounts))]

        def find_root(i):
            while uf[i] != i:
                i = uf[i]
            return i

        email_map = {}
        for i, (_, *emails) in enumerate(accounts):
            for email in emails:
                if email in email_map:
                    uf[find_root(email_map[email])] = i
                else:
                    email_map[email] = i
        ans = [set() for _ in range(len(accounts))]
        for i in range(len(accounts)):
            root = find_root(i)
            for email in accounts[i][1:]:
                ans[root].add(email)
        return [[accounts[i][0]] + sorted(s) for i, s in enumerate(ans) if s]
