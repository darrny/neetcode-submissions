class Solution:
    def trap(self, height: List[int]) -> int:
        res = 0
        l = 0
        r = len(height) - 1

        leftmax = height[l]
        rightmax = height[r]

        while l < r:
            left = height[l]
            right = height[r]


            if left < right:
                l += 1
                leftmax = max(leftmax, height[l])
                res += leftmax - height[l]

            elif left > right:
                r -= 1
                rightmax = max(rightmax, height[r])
                res += rightmax - height[r]

            else:
                l += 1
                leftmax = max(leftmax, height[l])
                res += leftmax - height[l]

        return res