# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        tree_one, tree_two = [], []
        
        self.inorder_traversal(p, tree_one)
        self.inorder_traversal(q, tree_two)
        
        return tree_one == tree_two
        
        
        
        
    def inorder_traversal(self, tree, tree_values):
        
        if tree is None:
            tree_values.append(None)
            return
            
        tree_values.append(tree.val)
        
        self.inorder_traversal(tree.left, tree_values)
        self.inorder_traversal(tree.right, tree_values)