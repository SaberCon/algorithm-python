class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        ans = []
        for i in range(1, n + 1):
            current = ''
            if not i % 3:
                current += 'Fizz'
            if not i % 5:
                current += 'Buzz'
            ans.append(current or str(i))
        return ans
