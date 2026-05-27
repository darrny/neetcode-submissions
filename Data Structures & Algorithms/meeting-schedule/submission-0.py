"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        intervals.sort(key = lambda i : i.start)
        n = len(intervals)

        for i in range(n - 1):
            start = intervals[i+1].start
            end = intervals[i].end

            if end > start:
                return False

        return True