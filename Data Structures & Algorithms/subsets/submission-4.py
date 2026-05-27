class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = [[]]

        for num in nums:
            res += [[num] + combi for combi in res]

        return res