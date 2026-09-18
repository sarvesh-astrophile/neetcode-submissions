# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        self.res = 0
        def good_nodes(node, max_val) -> int:
            if not node:
                return 0

            if node.val >= max_val:
                self.res += 1

            max_val = max(max_val, node.val)

            left = good_nodes(node.left, max_val)
            right = good_nodes(node.right, max_val)
            return self.res

        return good_nodes(root, root.val)
        