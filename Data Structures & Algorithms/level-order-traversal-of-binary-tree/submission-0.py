# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        res = []
        level = []
        level.append(root)
        while level:
            res.append([node.val for node in level])
            temp = []
            while level:
                curr = level.pop()
                if curr.right:
                    temp.append(curr.right)
                if curr.left:
                    temp.append(curr.left)
            while temp:
                level.append(temp.pop())
        return res