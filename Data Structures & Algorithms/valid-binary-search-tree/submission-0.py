# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        last = [-1000000001]
        
        def iot(root):
            if not root:
                return True
            
            left_bool = iot(root.left)

            if root.val <= last[0]:
                return False
            else:
                last[0] = root.val

            right_bool = iot(root.right)
            
            return left_bool and right_bool

        return iot(root)