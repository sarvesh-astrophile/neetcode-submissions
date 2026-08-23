# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        return self._depth(root)

    def _depth(self, node: TreeNode) -> int:
        if node:
            left = self._depth(node.left)
            right = self._depth(node.right) 
            ans = max(left, right)
            return 1 + ans
        else:
            return 0