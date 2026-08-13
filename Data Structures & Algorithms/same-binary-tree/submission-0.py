class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        self.result = True
        self._inorder(p, q)
        return self.result
        
    def _inorder(self, p: Optional[TreeNode], q: Optional[TreeNode]):
        if not self.result:
            return None
        if not p and not q:
            return None
        elif not p or not q:
            self.result = False
            return None

        self._inorder(p.left, q.left)
        
        if p.val != q.val:
            self.result = False

        self._inorder(p.right, q.right)