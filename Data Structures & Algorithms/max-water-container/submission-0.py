class Solution:
    def maxArea(self, heights: List[int]) -> int:
        n = len(heights)
        ret = 0
        l = 0
        r = n - 1

        while l < r:
            area = min(heights[l], heights[r]) * (r - l)
            ret = max(area, ret)

            if heights[l] < heights[r]:
                l += 1
            elif heights[r] < heights[l]:
                r -= 1
            else:
                l += 1

        return ret