# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findTarget(self, root: Optional[TreeNode], k: int) -> bool:
        sorted_list = []
        self.inorder(root, sorted_list)
        left = 0
        right = len(sorted_list) - 1
        
        while left < right:
            sum = sorted_list[left] + sorted_list[right]
            
            if sum == k:
                return True
            
            if sum > k:
                right -= 1
            
            else:
                left += 1
                
        return False
        
        
    def inorder(self, root, l) -> List:
        if not root:
            return
        
        self.inorder(root.left, l)
        l.append(root.val)
        self.inorder(root.right, l)
        
        


        
        