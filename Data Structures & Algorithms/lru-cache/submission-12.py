class ListNode:

    def __init__(self, key=0, val=0, prev=None, next=None):
        self.key = key
        self.val = val
        self.prev = prev
        self.next = next

class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache : dict(ListNode) = defaultdict(ListNode)

        self.head = ListNode()
        self.tail = ListNode()

        self.head.next = self.tail
        self.tail.prev = self.head

    def _remove(self, node: ListNode) -> None:
        previous = node.prev
        following = node.next
        previous.next = following
        following.prev = previous

    def _insert(self, node: ListNode) -> None:
        lastNode = self.tail.prev
        lastNode.next = node
        node.next = self.tail
        self.tail.prev = node
        node.prev = lastNode

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
            
        newNode = ListNode(key, value)
        self.cache[key] = newNode
        self._insert(newNode)

        if self.capacity < len(self.cache):
            lru = self.head.next
            self._remove(lru)
            del self.cache[lru.key]
        
