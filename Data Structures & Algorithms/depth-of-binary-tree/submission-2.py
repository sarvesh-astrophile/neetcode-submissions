class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        return self._depth(root)
        
    def _depth(self, node: Optional[TreeNode]) -> int:
        if node:
            return 1 + max(self._depth(node.left), self._depth(node.right))
        else:
            return 0