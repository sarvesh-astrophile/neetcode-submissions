# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        self.res = True
        self._isBalanced(root)
        return self.res

    def _isBalanced(self, node: Optional[TreeNode]) -> bool:
        if not node:
            return 0
        
        left = self._isBalanced(node.left)
        right = self._isBalanced(node.right)

        if abs(left - right) > 1:
            self.res = False

        return 1 + max(left, right)
