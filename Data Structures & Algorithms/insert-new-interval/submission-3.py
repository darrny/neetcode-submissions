import bisect

class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        stack = []
        intervals.insert(bisect.bisect_left(intervals, newInterval), newInterval)

        for interval in intervals:
            if not stack:
                stack.append(interval)
            
            earliest = interval[0]
            latest = interval[1]

            while stack and interval[0] <= stack[-1][1]:
                curr = stack.pop()
                earliest = min(earliest, curr[0])
                latest = max(latest, curr[1])

            stack.append([earliest, latest])

        return list(stack)
