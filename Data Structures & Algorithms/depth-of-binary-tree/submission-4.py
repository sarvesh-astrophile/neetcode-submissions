# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        return self._depth(root)
        
    def _depth(self, node: Optional[TreeNode]):
        if node:
            return 1 + max(self._depth(node.left), self._depth(node.right))
        else:
            return 0