# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        
        num1_str = ""
        current = l1
        while current:
            
            num1_str = str(current.val) + num1_str
            current = current.next

        num2_str = ""
        current = l2
        while current:
            
            num2_str = str(current.val) + num2_str
            current = current.next

        sum_num = int(num1_str) + int(num2_str)
        sum_str = str(sum_num)
        result_head = ListNode(int(sum_str[-1]))
        current = result_head

        for i in range(len(sum_str)-2,-1,-1):

            current.next = ListNode(int(sum_str[i]))
            current = current.next

        return result_head



