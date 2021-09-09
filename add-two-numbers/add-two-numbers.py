# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy_node = ListNode(0)
        current_node = dummy_node
        
        node_one = l1
        node_two = l2
        carry = 0
        
        while node_one is not None or node_two is not None or carry != 0:
            value_one = node_one.val if node_one is not None else 0
            value_two = node_two.val if node_two is not None else 0
            
            node_sum = value_one + value_two + carry
            
            new_node = ListNode(node_sum % 10)
            
            current_node.next = new_node
            current_node = new_node
            
            node_one = node_one.next if node_one is not None else None
            node_two = node_two.next if node_two is not None else None
            carry = node_sum // 10
            
        return dummy_node.next
        