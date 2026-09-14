# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        def dfs(node: TreeNode, max_val: int) -> int:
            if not node:
                return 0

            curr = 1 if node.val >= max_val else 0
            max_val = max(max_val, node.val)

            left = dfs(node.left, max_val)
            right = dfs(node.right, max_val)

            return curr + left + right

        return dfs(root, root.val)