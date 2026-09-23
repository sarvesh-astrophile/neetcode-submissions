# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def _isValidBST(node, high, low):
            if not node:
                return True

            if not (low < node.val < high):
                return False

            left = _isValidBST(node.left, node.val, low)
            right = _isValidBST(node.right, high, node.val)

            return left and right
            
        return _isValidBST(root, float('inf'), float('-inf'))