class Solution:
    def findAndReplacePattern(self, words: List[str], pattern: str) -> List[str]:
        def match(word):
            w_map, p_map = {}, {}
            for w, p in zip(word, pattern):
                if w not in w_map and p not in p_map:
                    w_map[w] = p
                    p_map[p] = w
                elif w not in w_map or p not in p_map or w_map[w] != p or p_map[p] != w:
                    return False
            return True

        return [word for word in words if match(word)]
