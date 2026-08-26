"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        intervals.sort(key=lambda x: x.start)
        
        stack = []
        for interval in intervals:
            if not stack:
                stack.append(interval)
            else:
                if interval.start < stack.pop().end:
                    return False
                stack.append(interval)
    
        return True