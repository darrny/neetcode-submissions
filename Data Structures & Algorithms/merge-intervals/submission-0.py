class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        stack = []
        intervals.sort()

        for interval in intervals:
            if not stack:
                stack.append(interval)

            else:
                
                earliest = interval[0]
                latest = interval[1]

                while stack and interval[0] <= stack[-1][1]:
                    curr = stack.pop()

                    earliest = min(curr[0], earliest)
                    latest = max(curr[1], latest)

                stack.append([earliest, latest])

        return list(stack)