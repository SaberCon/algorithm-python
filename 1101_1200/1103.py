class Solution:
    def distributeCandies(self, candies: int, num_people: int) -> List[int]:
        turns = int((2 * candies + 0.25) ** 0.5 - 0.5)
        remainder = candies - turns * (turns + 1) // 2
        rounds = turns // num_people
        last_round = turns % num_people

        ans = [0] * num_people
        for i in range(num_people):
            ans[i] = num_people * rounds * (rounds - 1) // 2 + rounds * (i + 1)
            if i < last_round:
                ans[i] += rounds * num_people + i + 1
        ans[last_round] += remainder
        return ans
