# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        total = 0
        path = ''
        total = self.dfs(root=root, path=path, total=total)
        
        return total
        
    
    def dfs(self, root: Optional[TreeNode], path: str, total: int) -> int:
        if not root:
            path = '0'
            return path
        
        if root.left is None and root.right is None:
            path += str(root.val)
            return path
        
        path += str(root.val)
        
        left_path = self.dfs(root.left, path, total)
        right_path = self.dfs(root.right, path, total)
        
        
        total = int(right_path) + int(left_path) 
        
        return total
        
        
        
        