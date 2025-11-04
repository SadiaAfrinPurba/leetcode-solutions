# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
from typing import List, Optional

class Solution:
    def modifiedList(self, nums: List[int], head: Optional[ListNode]) -> Optional[ListNode]:
        ban = set(nums)
        dummy = ListNode(0, head)
        curr = dummy

        while curr.next:
            if curr.next.val in ban:
                curr.next = curr.next.next   
            else:
                curr = curr.next             

        return dummy.next