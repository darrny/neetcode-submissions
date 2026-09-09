class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix_product = [nums[0]] * len(nums)
        for i in range(1, len(nums)):
            prefix_product[i] = prefix_product[i - 1] * nums[i]

        suffix_product = [nums[-1]] * len(nums)
        for i in range(len(nums) - 2, -1, -1):
            suffix_product[i] = suffix_product[i + 1] * nums[i]

        res = [0] * len(nums)
        res[0] = suffix_product[1]
        res[-1] = prefix_product[-2]
        
        for i in range(1, len(nums) - 1):
            res[i] = prefix_product[i - 1] * suffix_product[i + 1]
        
        return res