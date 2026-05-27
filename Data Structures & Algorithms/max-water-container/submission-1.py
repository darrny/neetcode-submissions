class Solution:
    def maxArea(self, heights: List[int]) -> int:
        res = 0
        n = len(heights)

        l = 0
        r = n - 1

        while l < r:

            leftWall = heights[l]
            rightWall = heights[r]

            area = min(leftWall, rightWall) * (r - l)
            res = max(area, res)

            if leftWall < rightWall:
                l += 1
            else:
                r -= 1


        return res