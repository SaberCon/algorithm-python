from collections import defaultdict


class Solution:
    def subdomainVisits(self, cpdomains: List[str]) -> List[str]:
        counts = defaultdict(lambda: 0)
        for cpdomain in cpdomains:
            count, domain = cpdomain.split()
            domains = domain.split('.')
            for i in range(len(domains)):
                counts['.'.join(domains[i:])] += int(count)
        return [str(count) + ' ' + domain for domain, count in counts.items()]
