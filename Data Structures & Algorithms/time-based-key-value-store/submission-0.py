class TimeMap:

    def __init__(self):
        self.map = defaultdict(list)

    def set(self, key, value, timestamp):
        """
        :type key: str
        :type value: str
        :type timestamp: int
        :rtype: None
        """
        self.map[key].append((timestamp, value))

    def get(self, key, timestamp):
        """
        :type key: str
        :type timestamp: int
        :rtype: str
        """
        arr = self.map[key]
        l, r = 0, len(arr) - 1
        ans = -1
        while l <= r:
            m = (l + r) // 2
            if arr[m][0] <= timestamp:
                ans = m
                l = m + 1
            else:
                r = m - 1
        if ans == -1:
            return ""
        timestamp, ret = self.map[key][ans]
        return ret
