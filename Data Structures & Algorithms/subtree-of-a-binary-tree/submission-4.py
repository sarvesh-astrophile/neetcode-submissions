# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        self.ans = False
        self._findNode(root, subRoot)
        return self.ans

    def _findNode(self, root: TreeNode, target: TreeNode) -> bool:
        if not target:
            self.ans = True
            return True

        if not root:
            return False

        if root.val == target.val:
            if self._isSame(root, target):
                self.ans = True
                return True

        left = self._findNode(root.left, target)
        right = self._findNode(root.right, target)
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