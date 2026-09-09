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

    def _findStart(self, root: TreeNode, target: TreeNode) -> bool:
        node = root
        if not node:
            return False

        left = self._findStart(node.left, target)
        right = self._findStart(node.right, target)

        if node.val == target.val:
            if self._isSame(node, target):
                self.res = True
                return True

        return left or right

    def _isSame(self, p: TreeNode, q: TreeNode) -> bool:
        if not p and not q:
            return True
        elif p and q and p.val == q.val:
            left = self._isSame(p.left, q.left)
            right = self._isSame(p.right, q.right)
            return left and right
        else:
            return False



