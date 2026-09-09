class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []

        def dfs(i: int, curr: List[int]) -> None:
            curr_sum = sum(curr)
            if curr_sum == target:
                res.append(curr.copy())
            elif curr_sum >= target:
                return
            else:
                for j in range(i, len(nums)):
                    curr.append(nums[j])
                    dfs(j, curr)
                    curr.pop()

        for k in range(len(nums)):
            dfs(k, [nums[k]])
        
        return res
