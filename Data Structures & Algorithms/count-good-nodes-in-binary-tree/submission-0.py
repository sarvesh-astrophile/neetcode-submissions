# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        self.res = 0
        self._countGood(root, root.val)
        return self.res

    def _countGood(self, node: TreeNode, maxVal: int) -> int:
        if not node:
            return 0

        curr = 1 if node.val >= maxVal else 0
        maxVal = max(maxVal, node.val)

        left = self._countGood(node.left, maxVal)
        right = self._countGood(node.right, maxVal)

        self.res = max(self.res, curr + left + right)

        return curr + left + right