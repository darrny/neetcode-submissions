# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:  

    def isSameTree(self, p, q):
        if not p and not q:
            return True
        if p and q and p.val == q.val:
            return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)
        return False

    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        seen = [root]

        while seen:
            curr = seen.pop()
            if self.isSameTree(curr, subRoot):
                return True
            if curr.left:
                seen.append(curr.left)
            if curr.right:
                seen.append(curr.right)

        return False
