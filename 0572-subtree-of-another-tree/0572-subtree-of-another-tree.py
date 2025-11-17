# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        def same_tree(node1, node2):
            if node1 == None and node2 == None:
                return True
            
            if (node1 and node2 == None) or (node2 and node1 == None):
                return False
            
            if node1.val != node2.val:
                return False
            return same_tree(node1.left, node2.left) and same_tree(node1.right, node2.right)

        def has_subtree(root):
            if not root:
                return False
            
            if same_tree(root, subRoot):
                return True
            
            return has_subtree(root.left) or has_subtree(root.right)
        return has_subtree(root)
        