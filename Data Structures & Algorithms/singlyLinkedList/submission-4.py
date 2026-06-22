class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next

class LinkedList:
    
    def __init__(self):
        self.head = Node(-1)
        self.tail = self.head
    
    def get(self, index: int) -> int:
        current = self.head.next

        i = 0
        while current:
            if i == index:
                return current.value
            i += 1
            current = current.next

        return -1

    def insertHead(self, val: int) -> None:
        newHead = Node(val)
        newHead.next = self.head.next
        self.head.next = newHead
        if not newHead.next:
            self.tail = newHead
        print(self.getValues())
        

    def insertTail(self, val: int) -> None:
        self.tail.next = Node(val)
        self.tail = self.tail.next
        print(self.getValues())
        

    def remove(self, index: int) -> bool:
        i = 0
        current = self.head
        while i < index and current:
            i += 1
            current = current.next

        if current and current.next:
            if current.next == self.tail:
                self.tail = current
            current.next = current.next.next
            print(self.getValues())
            return True
        
        print(self.getValues())
        return False

    def getValues(self) -> List[int]:
        valueList = []
        current = self.head.next
        
        if not current:
            return valueList
        
        while current:
            valueList.append(current.value)
            current = current.next
        
        return valueList
        
