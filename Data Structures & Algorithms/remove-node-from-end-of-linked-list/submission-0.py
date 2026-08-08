# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        start = end = head
        dummy = ListNode()
        dummy.next = head
        prev = dummy

        for i in range(n):
            end = end.next

        while end:
            prev = start
            start = start.next
            end = end.next

        prev.next = start.next
        start.next = None

        return dummy.next

        
        