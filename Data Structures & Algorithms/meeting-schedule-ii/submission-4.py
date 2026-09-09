"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        intervals.sort(key = lambda x: x.start)
        rooms = []
        maximum = 0

        for interval in intervals:
            if not rooms:
                rooms.append((interval.end, interval.start))
            else:
                if interval.start < rooms[0][0]:
                    heapq.heappush(rooms, (interval.end, interval.start))
                else:
                    heapq.heappop(rooms)
                    heapq.heappush(rooms, (interval.end, interval.start))
            
            maximum = max(maximum, len(rooms))

        return maximum

