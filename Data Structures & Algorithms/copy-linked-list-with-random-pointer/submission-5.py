"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""


class Solution:
    def copyRandomList(self, head: "Optional[Node]") -> "Optional[Node]":
        # copy to dict
        copyDict: dict(Node) = {None: None}

        # make node and add to copyDict
        curr = head
        while curr:
            node = Node(x=curr.val)
            copyDict[curr] = node
            curr = curr.next

        # link all nodes
        curr = head
        while curr:
            copy = copyDict[curr]
            copy.next = copyDict[curr.next]
            copy.random = copyDict[curr.random]
            curr = curr.next

        return copyDict[head]

