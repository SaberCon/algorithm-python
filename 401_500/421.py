class Solution:
    def findMaximumXOR(self, nums: List[int]) -> int:
        length = len(bin(max(nums))) - 2

        max_xor = 0
        trie = {}
        for num in nums:
            node = trie
            xor_node = trie
            curr_xor = 0
            for i in range(length)[::-1]:
                bit = (num >> i) & 1
                if bit not in node:
                    node[bit] = {}
                node = node[bit]

                toggled_bit = 1 - bit
                curr_xor <<= 1
                if toggled_bit in xor_node:
                    curr_xor += 1
                    xor_node = xor_node[toggled_bit]
                else:
                    xor_node = xor_node[bit]
            max_xor = max(max_xor, curr_xor)
        return max_xor
