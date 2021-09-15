"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, next=None):
        self.val = val
        self.next = next
"""

class Solution:
    def insert(self, head: 'Node', insertVal: int) -> 'Node':
        if not head:
            node = Node()
            node.val = insertVal
            node.next = node
            return node
        
        current = max_node = head
        
        while not current.val <= insertVal <= current.next.val:
            if current.val >= max_node.val:
                max_node = current
            
            current = current.next
            
            if current == head:
                current = max_node
                break
                
        next_node = current.next
        new_node = Node()
        new_node.val = insertVal
        current.next = new_node
        new_node.next = next_node
        
        return head
        
        