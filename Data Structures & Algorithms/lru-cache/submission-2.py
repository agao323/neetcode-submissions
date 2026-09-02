class LRUNode:
    def __init__(
        self, 
        key: int,
        val: int, 
        prev: Optional[LRUNode] = None, 
        nxt: Optional[LRUNode] = None
    ):
        self.key = key
        self.val = val
        self.prev = prev
        self.nxt = nxt

class LRUCache:
    """
    TIME:
        33:53 - implementation pretty rough

    doubly linked list + hashmap
    create a new class with prev/next/val
    track the head and tail nodes
        do this with dummy nodes that don't get
        removed from the hashmap or ll
    get:
        fetch the object from the hashmap
        return the value stored inside
        move to the front of the linked list
        connect original prev/next in linked list
    put:
        if key exists:
            fetch from hashmap and update value
            move to front of linked list
            connect original prev/next in linked list
        if key doesn't exist:
            add to hashmap
            if current_capacity == max:
                remove tail
                add new head
    """
    HEAD = -1
    TAIL = -2

    def __init__(self, capacity: int):
        self.max_capacity = capacity
        self.current_capacity = 0

        self.head = LRUNode(LRUCache.HEAD, 0)
        self.tail = LRUNode(LRUCache.TAIL, 0)
        self.head.nxt = self.tail
        self.tail.prev = self.head

        self.hashmap = {
            LRUCache.HEAD: self.head,
            LRUCache.TAIL: self.tail
        }

    def updateHead(self, node: LRUNode) -> None:
        node.prev = self.head
        node.nxt = self.head.nxt
        self.head.nxt.prev = node
        self.head.nxt = node
    
    def extractNode(self, node: LRUNode) -> None:
        node.prev.nxt = node.nxt
        node.nxt.prev = node.prev

    def get(self, key: int) -> int:
        if key not in self.hashmap:
            return -1

        node = self.hashmap[key]
        self.extractNode(node)
        self.updateHead(node)
        return node.val
        
    def put(self, key: int, value: int) -> None:
        if key in self.hashmap:
            node = self.hashmap[key]
            self.extractNode(node)
            self.updateHead(node)
            node.val = value
        else:
            new_node = LRUNode(key, value)
            self.hashmap[key] = new_node
            self.current_capacity += 1

            if self.current_capacity > self.max_capacity:
                # evict the least recently used node (tail.prev)
                evict = self.tail.prev
                self.extractNode(evict)
                del self.hashmap[evict.key]

            self.updateHead(new_node)
        
        
