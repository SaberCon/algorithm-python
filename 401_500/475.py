class Solution:
    def findRadius(self, houses: [int], heaters: [int]) -> int:
        houses.sort()
        heaters.append(-10 ** 10)
        heaters.append(10 ** 20)
        heaters.sort()

        def find_nearest(pos, left, right):
            if right - left == 1:
                return left if pos - heaters[left] < heaters[right] - pos else right
            mid = (left + right) // 2
            if pos < heaters[mid]:
                return find_nearest(pos, left, mid)
            else:
                return find_nearest(pos, mid, right)

        radius = 0
        start = 0
        for house in houses:
            start = find_nearest(house, start, len(heaters) - 1)
            radius = max(radius, abs(heaters[start] - house))
        return radius
