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

    def _findStart(self, root: TreeNode, target: Target):
        if not target:
            self.res = True
            return True

        if not root:
            return False

        if root and target and root.val == target.val:
            if self._isSame(root, target):
                self.res = True
                return True


        left = self._findStart(root.left, target)
        right = self._findStart(root.right, target)
        return left or right

    def _isSame(self, root: TreeNode, subRoot: TreeNode):
        if not root and not subRoot:
            return True

        if not root or not subRoot or root.val != subRoot.val:
            return False

        left = self._isSame(root.left, subRoot.left)
        right = self._isSame(root.right, subRoot.right)

        return left and right
