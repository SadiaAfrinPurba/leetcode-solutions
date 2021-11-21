# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        inorder_value_to_index_mapper = {val:idx for idx, val in enumerate(inorder)}
        
        self.index = 1
        
        def build(left, right):
            
            if left > right:
                return None
            
            root = TreeNode(postorder[-self.index]) 
            self.index += 1
           
            root_idx = inorder_value_to_index_mapper[root.val]
            
            root.right = build(root_idx + 1, right)
            root.left = build(left, root_idx - 1)
            
            return root
        
         
        return build(0, len(inorder) - 1)
        
    