# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        # Find middle
        slow = fast = head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        # reverse the 2nd half
        curr = slow.next 
        prev = None
        slow.next = None

        while curr:
            tmp = curr.next
            curr.next = prev
            prev = curr
            curr = tmp

        # merge halves
        first = head
        second = prev

        while second:
            first_tmp = first.next
            second_tmp = second.next

            first.next = second
            second.next = first_tmp

            first = first_tmp
            second = second_tmp