class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.ans = 0
        self._depth(root)
        return self.ans

    def _depth(self, node: Optional[TreeNode]) -> int:
        if node:
            left = self._depth(node.left)
            right = self._depth(node.right)
            self.ans = max(self.ans, left + right)
            return 1 + max(left, right)
        else:
            return 0