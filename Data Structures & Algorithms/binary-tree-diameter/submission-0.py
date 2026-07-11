# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        diameter=0
        def count_height(root):
            nonlocal diameter
            if root == None:
                return 0
            else:
                left = count_height(root.left) 
                right = count_height(root.right)   
                diameter = max(diameter, left+right)  

            return max(left,right)+1
        
        count_height(root)
        return diameter
    
            