# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        slow_node, fast_node = head, head
        
        while fast_node is not None and fast_node.next is not None:
            slow_node = slow_node.next
            fast_node = fast_node.next.next
        
        reverse_second_half = self.reverse_linked_list(slow_node)
        first_half = head
        
        while reverse_second_half is not None:
            if reverse_second_half.val != first_half.val:
                return False
            
            reverse_second_half = reverse_second_half.next
            first_half = first_half.next
            
        return True
            
        
        
    def reverse_linked_list(self, head) -> ListNode:
        previous_node, current_node = None, head
        
        while current_node is not None:
            next_node = current_node.next
            current_node.next = previous_node
            previous_node = current_node
            current_node = next_node
        return previous_node
        