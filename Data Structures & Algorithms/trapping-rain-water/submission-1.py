class Solution:
    def trap(self, height: List[int]) -> int:
        l = 0
        r = len(height) - 1
        lmax = height[l]
        rmax = height[r]
        vol = 0

        while l < r:

            if height[l] < height[r]:
                l += 1
                lmax = max(height[l], lmax)
                vol += lmax - height[l]
            else:
                r -= 1
                rmax = max(height[r], rmax)
                vol += rmax - height[r]

        return vol