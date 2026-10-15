# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        
        length = 0

        curr = head
        while curr:
            length += 1
            curr = curr.next

        # the nth node from the end is the same as the N-n node from the front
        
        dummy = ListNode(0, head)  #dummy
        curr = dummy
        count = 0

        for i in range(length-n):
            curr = curr.next #node before target

        curr.next = curr.next.next

        return dummy.next
        

        # One pass solution: Two pointers, set window length of n and then move both pointer to the end. But same complexity