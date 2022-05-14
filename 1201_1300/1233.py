from typing import List


class Solution:
    def removeSubfolders(self, folder: List[str]) -> List[str]:
        trie = {}
        ans = []
        for f in sorted(folder, key=len):
            pos = trie
            for sub in f[1:].split('/'):
                if sub not in pos:
                    pos[sub] = {}
                pos = pos[sub]
                if 'E' in pos:
                    break
            else:
                pos['E'] = True
                ans.append(f)
        return ans
