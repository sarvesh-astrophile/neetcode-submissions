# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def _checkBST(node: TreeNode, low: float, high: float) -> bool:
            if not node:
                return True

            if not (low < node.val < high):
                return False
                
            left = _checkBST(node.left, low, node.val)
            right = _checkBST(node.right, node.val, high)

            return left and right
        return _checkBST(root, float('-inf'), float('inf'))