# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.ans = 0
        self._diameter(root)
        return self.ans

    def _diameter(self, node: TreeNode) -> int:
        if node:
            left = self._diameter(node.left)
            right = self._diameter(node.right)
            self.ans = max(self.ans, left + right)
            return 1 + max(left, right)
        else:
            return 0
