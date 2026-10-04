# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        global_maximum = root.val
        memo = {}

        def dfs(root):
            if root is None:
                return 0
            if root in memo:
                return memo[root]

            nonlocal global_maximum
            curr_sum = max(
                root.val,
                root.val + dfs(root.right),
                root.val + dfs(root.left),
            )

            global_maximum = max(
                global_maximum,
                curr_sum,
                root.val + dfs(root.right) + dfs(root.left)
            )
            
            if curr_sum < 0:
                memo[root] = 0
                return 0

            memo[root] = curr_sum
            return curr_sum

        dfs(root)
        return global_maximum