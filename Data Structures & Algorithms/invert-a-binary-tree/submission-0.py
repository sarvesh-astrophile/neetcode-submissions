# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        # init 
        # use temp to invert
        self._invert(root)
        return root

    def _invert(self, node: Optional[TreeNode]):
        if not node:
            return -1

        temp1 = node.left
        temp2 = node.right

        node.left = temp2
        node.right = temp1

        self._invert(temp1)
        self._invert(temp2)