# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        self.res = False
        self._findStart(root, subRoot)
        return self.res

    def _findStart(self, root: TreeNode, node: TreeNode):
        if root is None:
            return False

        if root.val == node.val:
            if self._isSame(root, node):
                self.res = True
                return True

        left = self._findStart(root.left, node)
        right = self._findStart(root.right, node)
        return left or right

    def _isSame(self, p: TreeNode, q: TreeNode) -> bool:
        if not p and not q:
            return True

        if p and q and p.val == q.val:
            left = self._isSame(p.left, q.left)
            right = self._isSame(p.right, q.right)
            return left and right
        else:
            return False