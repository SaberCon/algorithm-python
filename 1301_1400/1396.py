class UndergroundSystem:

    def __init__(self):
        self.ins = {}
        self.travels = {}

    def checkIn(self, id: int, stationName: str, t: int) -> None:
        self.ins[id] = (stationName, t)

    def checkOut(self, id: int, stationName: str, t: int) -> None:
        start_station, start_time = self.ins[id]
        del self.ins[id]
        travel = (start_station, stationName)
        if travel in self.travels:
            self.travels[travel][0] += t - start_time
            self.travels[travel][1] += 1
        else:
            self.travels[travel] = [t - start_time, 1]

    def getAverageTime(self, startStation: str, endStation: str) -> float:
        duration, count = self.travels[startStation, endStation]
        return duration / count
