class Node:
    def __init__(self, key: int, value: int) -> None:
        self.key = key
        self.value = value
        self.prev = None
        self.next = None


class LRUCache:
    def __init__(self, capacity: int) -> None:
        self.capacity = capacity
        self.cache: dict[int, Node] = {}  # key -> node

        # Dummy head (left) and tail (right) to simplify list operations
        self.head = Node(0, 0)
        self.tail = Node(0, 0)
        self.head.next = self.tail
        self.tail.prev = self.head

    def _remove(self, node: Node) -> None:
        previous = node.prev
        following = node.next
        previous.next = following
        following.prev = previous

    def _insert(self, node: Node) -> None:
        before_tail = self.tail.prev
        before_tail.next = node
        node.prev = before_tail
        node.next = self.tail
        self.tail.prev = node

    def get(self, key: int) -> int:
        if key in self.cache:
            node = self.cache[key]
            self._remove(node)
            self._insert(node)
            return node.value
        return -1

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            # Remove existing node to re-insert it in the correct position
            self._remove(self.cache[key])

        new_node = Node(key, value)
        self.cache[key] = new_node
        self._insert(new_node)

        if len(self.cache) > self.capacity:
            # Evict the least recently used node (first real node after head)
            lru_node = self.head.next
            self._remove(lru_node)
            del self.cache[lru_node.key]