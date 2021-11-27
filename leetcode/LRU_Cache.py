class LNode():
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.next = None
        self.prev = None


class LRUCache(object):
    def __init__(self, capacity):
        self.capacity = capacity
        self.map = {}
        self.head = LNode("#", "#")
        self.tail = LNode("#", "#")
        self.head.next = self.tail
        self.tail.prev = self.head

    def _add(self, key, node):
        temp = self.head.next
        self.head.next = node
        node.prev = self.head
        node.next = temp
        temp.prev = node
        self.map[key] = node

        # eviction
        if len(self.map) > self.capacity:
            self._remove(self.tail.prev)

    def _remove(self, node):
        node.prev.next = node.next
        node.next.prev = node.prev
        node.next = None
        node.prev = None
        del self.map[node.key]

    def get(self, key):
        if key in self.map:
            node = self.map[key]
            self._remove(node)
            self._add(key,node)
            return node.val
        else:
            return -1

    def put(self, key, value):
        if key in self.map:
            node = self.map[key]
            self._remove(node)
            self._add(key, node)
            node.val = value
        else:
            node = LNode(key, value)
            self._add(key, node)


c = LRUCache(2)
c.put(1,1)
c.put(2,2)
print(c.get(1))
c.put(3,3)
print(c.get(2))
c.put(4,4)
print(c.get(1))
print(c.get(3))
print(c.get(4))

