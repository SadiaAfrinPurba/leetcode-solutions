# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        length = 0
        
        temp = head
        
        while temp:
            length += 1
            
            temp = temp.next
        
        mid = (length // 2) + 1
        
        for i in range(1, mid):
            head = head.next
        
        return head