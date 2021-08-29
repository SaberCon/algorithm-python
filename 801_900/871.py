class Solution:
    def minRefuelStops(self, target: int, startFuel: int, stations: List[List[int]]) -> int:
        dp = {0: startFuel}
        current = 0
        for p, f in stations + [(target, 0)]:
            new_dp = {}
            for stops, fuel in dp.items():
                cost = p - current
                if fuel < cost:
                    continue
                if stops not in new_dp or fuel - cost > new_dp[stops]:
                    new_dp[stops] = fuel - cost
                if (stops + 1) not in new_dp or fuel - cost + f > new_dp[stops + 1]:
                    new_dp[stops + 1] = fuel - cost + f
            dp = new_dp
            current = p
        return min(dp.keys()) if dp else -1
