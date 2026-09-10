class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort()
        stack1 = []
        stack2 = []

        print(intervals)

        for interval in intervals:
            if not stack1:
                stack1.append(interval)
            elif interval[0] < stack1[-1][1]:
                continue
            else:
                stack1.append(interval)

        for interval in intervals[::-1]:
            if not stack2:
                stack2.append(interval)
            elif interval[1] > stack2[-1][0]:
                continue
            else:
                stack2.append(interval)

        return min(len(intervals) - len(stack1), len(intervals) - len(stack2))