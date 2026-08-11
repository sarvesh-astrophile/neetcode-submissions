class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        # init 
        # use temp to invert
        self._invert(root)
        return root

    def _invert(self, node: Optional[TreeNode]):
        if not node:
            return

        temp1 = node.left
        temp2 = node.right

        node.left = temp2
        node.right = temp1

        self._invert(temp1)
        self._invert(temp2)