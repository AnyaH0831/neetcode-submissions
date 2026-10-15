# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        
        fast = head
        slow = head

        while fast != None and slow != None:

            if slow.next and fast.next and fast.next.next:
                slow = slow.next
                fast = fast.next.next
            else:
                return False

            if fast == slow and slow != None and fast != None:
                return True


        return False