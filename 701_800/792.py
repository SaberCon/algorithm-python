from collections import defaultdict


class Solution:
    def numMatchingSubseq(self, S: str, words: List[str]) -> int:
        word_dict = defaultdict(list)
        for word in words:
            word_dict[word[0]].append(word)
        ans = 0
        for c in S:
            word_list = word_dict[c]
            word_dict[c] = []
            for word in word_list:
                if len(word) == 1:
                    ans += 1
                else:
                    word_dict[word[1]].append(word[1:])
        return ans
