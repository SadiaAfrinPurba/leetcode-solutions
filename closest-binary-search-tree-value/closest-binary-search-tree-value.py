# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def closestValue(self, root: Optional[TreeNode], target: float) -> int:
        
        closest = root.val
        current = root
        
        while current is not None:
            if abs(target - closest) > abs(target - current.val):
                closest = current.val
                
            if target > current.val:
                current = current.right
                
            elif target < current.val:
                current = current.left
                
            else:
                break
        return closest
        