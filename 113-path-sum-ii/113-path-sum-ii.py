# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        if not root:
            return []
        
        stack = [(root, [root.val])]
        ans = []        
        while stack:
            current, nodes  = stack.pop()

            if not current.left and not current.right and sum(nodes) ==  targetSum:
                    ans.append(nodes)
                
            if current.left:
                stack.append((current.left, nodes + [current.left.val]))
            
            if current.right:
                stack.append((current.right, nodes +  [current.right.val]))
        
        return ans
            
        
        
            
            
            
        