class TimeMap:

    def __init__(self):
        self.kv = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.kv[key].append([value, timestamp])

    def get(self, key: str, timestamp: int) -> str:
        values = self.kv[key]
        result = ""
        l, r = 0, len(values) -1
        while l <= r:
            mid = l + (r - l) // 2

            if timestamp >= values[mid][1]:
                result = values[mid][0]
                l = mid + 1
            else:
                r = mid - 1

        return result
