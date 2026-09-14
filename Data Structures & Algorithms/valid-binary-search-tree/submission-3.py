# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        self.res = True
        self._dfs(root, float('-inf'), float('inf'))
        return self.res
    
    def _dfs(self, node: TreeNode, lowerbond: float, upperbond: float) -> bool:
        if not node:
            return True

        left = self._dfs(node.left, lowerbond, node.val)
        right = self._dfs(node.right, node.val, upperbond)

        if not(node.val < upperbond and node.val > lowerbond):
            self.res = False
            return False

        return left and right