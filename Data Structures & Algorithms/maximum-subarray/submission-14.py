class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        currSum = float('-inf')
        res = currSum
        
        for num in nums:
            if num > currSum and currSum > 0:
                currSum += num
            elif num > currSum:
                currSum = num
            else:
                currSum += num
            res = max(res, currSum)

        return res