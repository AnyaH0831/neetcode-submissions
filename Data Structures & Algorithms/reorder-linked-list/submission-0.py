# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        
        slow, fast = head, head

        while fast.next and fast.next.next:
            
            slow = slow.next
            fast = fast.next.next

        # slow is at midpoint
        start = slow.next
        
        slow.next = None
        curr = start
        prev = None
        while curr:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp

        # two reversed linkedlist
        reverse = prev
        curr = head
        while reverse:

            temp1 = curr.next
            temp2 = reverse.next

            curr.next = reverse

            reverse.next = temp1

            curr = temp1
            reverse = temp2



