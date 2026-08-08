# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        start = end = dummy

        for i in range(n+1):
            end = end.next

        while end:
            start = start.next
            end = end.next

        start.next = start.next.next

        return dummy.next

        
        