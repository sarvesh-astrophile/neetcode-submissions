class ListNode:

    def __init__(self, key=0, val=0, prev=None, next=None):
        self.key = key
        self.val = val
        self.prev = prev
        self.next = next

class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache: dict[int, ListNode] = {}

        self.head, self.tail = ListNode(), ListNode()
        self.head.next = self.tail
        self.tail.prev = self.head

    def _remove(self, node: ListNode) -> None:
        previous = node.prev
        following = node.next
        previous.next = following
        following.prev = previous

    def _insert(self, node: ListNode) -> None:
        lastnode = self.tail.prev

        lastnode.next = node
        node.next = self.tail

        self.tail.prev = node
        node.prev = lastnode
        
    def get(self, key: int) -> int:
        if key in self.cache:
            node = self.cache[key]
            self._remove(node)
            self._insert(node)
            return node.val
        else:
            return -1

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            node = self.cache[key]
            self._remove(node)

        new_node = ListNode(key, value)
        self.cache[key] = new_node
        self._insert(new_node)

        # lru
        if len(self.cache) > self.capacity:
            lru_node = self.head.next
            self._remove(lru_node)
            del self.cache[lru_node.key]
