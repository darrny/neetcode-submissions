class Solution:
    def maxArea(self, heights: List[int]) -> int:
        left = 0
        right = len(heights) - 1
        curr = 0

        while left < right:
            curr = max(min(heights[left], heights[right]) * (right - left), curr)

            if heights[left] < heights[right]:
                left += 1
            elif heights[left] > heights[right]:
                right -= 1
            else:
                right -=1
                left += 1

        return curr