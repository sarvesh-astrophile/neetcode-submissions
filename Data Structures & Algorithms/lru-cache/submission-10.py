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

    def _insert(self, node: ListNode):
        last_node = self.tail.prev
        last_node.next = node
        node.next = self.tail
        self.tail.prev = node
        node.prev = last_node

    def _remove(self, node: ListNode):
        previous = node.prev
        following = node.next
        previous.next = following
        following.prev = previous

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

        new_node = ListNode(key=key, val=value)
        self.cache[key] = new_node
        self._insert(new_node)

        # lru
        if len(self.cache) > self.capacity:
            lru = self.head.next
            self._remove(lru)
            del self.cache[lru.key]
