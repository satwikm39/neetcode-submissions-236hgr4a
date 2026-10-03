class Node:
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.prev = self.next = None

class LRUCache:
    def __init__(self, capacity):
        self.cap = capacity
        self.cache = {}
        self.left, self.right = Node(0, 0), Node(0, 0)
        self.left.next = self.right
        self.right.prev = self.left

    def insert(self, node: Node):
        new_second = self.right.prev
        new_second.next = node
        node.prev = new_second
        node.next = self.right
        self.right.prev = node

    def remove(self, node: Node):
        prev = node.prev
        prev.next = node.next
        node.next.prev = prev

    
    def get(self, key: int) -> int:
        if key in self.cache:
            node = self.cache[key]
            self.remove(node)
            self.insert(node)
            return node.val
        return -1

    def put(self, key: int, val: int) -> None:
        if key in self.cache:
            self.remove(self.cache[key])

        node = Node(key, val)
        self.cache[key] = node
        self.insert(node)

        if len(self.cache) > self.cap:
            lru = self.left.next
            self.remove(lru)
            self.cache.pop(lru.key)

