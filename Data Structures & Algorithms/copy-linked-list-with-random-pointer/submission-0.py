"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        
        if not head:
            return None
        current = head.next
        newNode = Node(head.val)
        copyMap = {}
        copyMap[head] = newNode
        while current: 
            
            new = Node(current.val)

            newNode.next = new

            copyMap[current] = new

            newNode = newNode.next

            current = current.next
        newNode.next = None

        current = head
        newHead = copyMap[head]
        newCurrent = newHead
        while current: 

            if current.random:
                newCurrent.random = copyMap[current.random]

            newCurrent = newCurrent.next
            current = current.next

        return newHead





