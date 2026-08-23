class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        self.ans = True
        self._balance(root)
        return self.ans

    def _balance(self, node: Optional[TreeNode]) -> int:
        if not node:
            return 0

        left_depth = self._balance(node.left)
        right_depth = self._balance(node.right)

        if abs(left_depth - right_depth) > 1:
            self.ans = False

        return 1 + max(left_depth, right_depth)