class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        five = ten = 0
        for bill in bills:
            if bill == 5:
                five += 1
            if bill == 10:
                if five < 1:
                    return False
                five -= 1
                ten += 1
            if bill == 20:
                if five > 0 and ten > 0:
                    five -= 1
                    ten -= 1
                elif five > 2:
                    five -= 3
                else:
                    return False
        return True
