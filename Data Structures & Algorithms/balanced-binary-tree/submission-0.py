# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        self.result = True
        self._depth(root)
        return self.result
        
    def _depth(self, node: Optional[TreeNode]) -> int:
        if not node:
            return 0
        else:
            left = self._depth(node.left)
            right = self._depth(node.right)
            if abs(left - right) > 1:
                self.result = False
                return 0
            return 1 + max(left, right)
