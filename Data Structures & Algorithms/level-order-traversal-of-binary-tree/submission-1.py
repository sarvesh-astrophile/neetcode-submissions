# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        self.result = defaultdict(list)
        self._levelOrder(root, 0)
        return list(self.result.values())

    def _levelOrder(self, node: TreeNode, level: int) -> None:
        if not node:
            return

        self.result[level].append(node.val)
        self._levelOrder(node.left, level + 1)
        self._levelOrder(node.right, level + 1)