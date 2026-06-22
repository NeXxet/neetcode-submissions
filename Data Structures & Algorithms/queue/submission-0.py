class Node:
    
    def __init__(self, value, next=None, prev=None):
        self.value = value
        self.next = next
        self.prev = prev

class Deque:
    
    def __init__(self):
        self.head = Node(-1)
        self.tail = Node(-1)
        self.head.next = self.tail
        self.tail.prev = self.head


    def isEmpty(self) -> bool:
        return self.head.next == self.tail
        

    def append(self, value: int) -> None:
        newNode = Node(value)
        self.tail.prev.next = newNode
        newNode.prev = self.tail.prev
        newNode.next = self.tail
        self.tail.prev = newNode


    def appendleft(self, value: int) -> None:
        newNode = Node(value)
        self.head.next.prev = newNode
        newNode.next = self.head.next
        self.head.next = newNode
        newNode.prev = self.head


    def pop(self) -> int:
        if self.isEmpty():
            return -1

        poppedNode = self.tail.prev

        poppedNode.prev.next = self.tail
        self.tail.prev = poppedNode.prev

        poppedNode.prev = None
        poppedNode.next = None
        
        return poppedNode.value

    def popleft(self) -> int:
        if self.isEmpty():
            return -1

        poppedNode = self.head.next

        self.head.next = poppedNode.next
        poppedNode.next.prev = self.head

        poppedNode.prev = None
        poppedNode.next = None

        return poppedNode.value





        
