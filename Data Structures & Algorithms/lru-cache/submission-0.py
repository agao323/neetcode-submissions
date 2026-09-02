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

    def get(self, key: int) -> int:
        if key not in self.hashmap:
            return -1

        node = self.hashmap[key]

        # reconnect the old positions
        old_prev, old_nxt = node.prev, node.nxt
        old_prev.nxt = old_nxt
        old_nxt.prev = old_prev

        # insert the new head
        tmp_next = self.head.nxt
        node.prev = self.head
        node.nxt = tmp_next
        tmp_next.prev = node
        self.head.nxt = node

        return node.val
        

    def put(self, key: int, value: int) -> None:
        if key in self.hashmap:
            node = self.hashmap[key]
            node.val = value

            # reconnect the old positions
            old_prev, old_nxt = node.prev, node.nxt
            old_prev.nxt = old_nxt
            old_nxt.prev = old_prev

            # insert the new head
            tmp_next = self.head.nxt
            node.prev = self.head
            node.nxt = tmp_next
            tmp_next.prev = node
            self.head.nxt = node
        else:
            new_node = LRUNode(key, value)
            self.hashmap[key] = new_node
            self.current_capacity += 1

            if self.current_capacity > self.max_capacity:
                # evict the least recently used node (tail.prev)
                cur_tail = self.tail.prev
                cur_tail_prev = cur_tail.prev
                cur_tail_prev.nxt = self.tail
                self.tail.prev = cur_tail_prev
                del self.hashmap[cur_tail.key]

            # insert the new head
            tmp_next = self.head.nxt
            new_node.prev = self.head
            new_node.nxt = tmp_next
            tmp_next.prev = new_node
            self.head.nxt = new_node
        
        
