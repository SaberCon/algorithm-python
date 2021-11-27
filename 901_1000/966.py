class Solution:
    def spellchecker(self, wordlist: List[str], queries: List[str]) -> List[str]:
        words = set(wordlist)
        lowers = {w.lower(): w for w in reversed(wordlist)}
        errors = {w.lower().replace('e', 'a').replace('i', 'a').replace('o', 'a').replace('u', 'a'): w for w in
                  reversed(wordlist)}

        ans = []
        for q in queries:
            if q in words:
                ans.append(q)
                continue
            q = q.lower()
            if q in lowers:
                ans.append(lowers[q])
                continue
            q = q.replace('e', 'a').replace('i', 'a').replace('o', 'a').replace('u', 'a')
            if q in errors:
                ans.append(errors[q])
                continue
            ans.append('')
        return ans
