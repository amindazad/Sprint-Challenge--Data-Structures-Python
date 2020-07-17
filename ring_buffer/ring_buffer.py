class ListNode:
    def __init__(self, value, prev=None, next=None):
        self.value = value
        self.prev = prev
        self.next = next

    def insert_after (self, value):
        current_next = self.next
        self.next = ListNode(self, value, current_next)
        if current_next:
            current_next.prev = self.next
    
    def insert_before (self, value):
        current_prev = self.prev
        self.prev = ListNode(self, value, current_prev)
        if current_prev:
            current_prev.next = self.prev
    
    def delete(self):
        if self.prev:
            self.prev.next = self.next
        if self.next:
            self.next.prev = self.prev

class DLL:
    def __init__(self, node = None):
        self.head = node
        self.tail = node
        self.length = 1 if node is not None else 0
    
    def __len__(self):
        return self.length

    def add_to_tail (self, value):
        new_node = ListNode(value, None, None)
        self.length += 1

        if self.tail:
            new_node.prev = self.tail
            self.tail.next = new_node
            self.tail = new_node
        
        else:
            self.head = new_node

        self.tail = new_node

class RingBuffer:
    def __init__(self, capacity):
        self.capacity = capacity
        self.oldest = None
        self.buffer = DLL()

    def append(self, item):
        pass

    def get(self):
        pass