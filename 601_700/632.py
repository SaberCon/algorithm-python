class Solution:
    def smallestRange(self, nums: List[List[int]]) -> List[int]:
        num_dict = {}
        for i, num_list in enumerate(nums):
            for num in num_list:
                num_dict.setdefault(num, set())
                num_dict[num].add(i)
        num_cover = sorted(num_dict.items(), key=lambda item: item[0])
        ans = [-100000, 100000]
        included = {}
        curr = -1
        for num, cover in num_cover:
            while len(included) < len(nums):
                curr += 1
                if curr == len(num_cover):
                    return ans
                for i in num_cover[curr][1]:
                    included[i] = included.get(i, 0) + 1
            if num_cover[curr][0] - num < ans[1] - ans[0]:
                ans = [num, num_cover[curr][0]]
            for i in cover:
                if included[i] == 1:
                    del included[i]
                else:
                    included[i] -= 1
        return ans
