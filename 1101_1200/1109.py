class Solution:
    def corpFlightBookings(self, bookings: List[List[int]], n: int) -> List[int]:
        fights = [0] * n
        for first, last, seats in bookings:
            fights[first - 1] += seats
            if last < n:
                fights[last] -= seats
        ans = [0] * n
        total = 0
        for i, booking in enumerate(fights):
            total += booking
            ans[i] = total
        return ans
