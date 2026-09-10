# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        counter = [0]
        
        def dfs(root, k):
            if root is not None:
                left = dfs(root.left, k)
                if left is not None:
                    return left

                counter[0] += 1
                if counter[0] == k:
                    return root.val

                right = dfs(root.right, k)
                if right is not None:
                    return right

        return dfs(root, k)
