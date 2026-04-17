from collections import defaultdict
from sortedcontainers import SortedDict

class TimeMap:
    
    def __init__(self):
        self.timeMap = defaultdict(SortedDict)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.timeMap[key][timestamp] = value
        # print(self.timeMap)

    def get(self, key: str, timestamp: int) -> str:
        
        if key not in self.timeMap:
            return ""

        timestamps = self.timeMap[key]
        # key -- timestamp; value -- value

        idx = timestamps.bisect_right(timestamp) - 1

        if idx >= 0:
            closest_time = timestamps.keys()[idx]
            return timestamps[closest_time]
        return ""


