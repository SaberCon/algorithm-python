class Solution:
    def distanceBetweenBusStops(self, distance: List[int], start: int, destination: int) -> int:
        return min(d := sum(distance[min(start, destination):max(start, destination)]), sum(distance) - d)
