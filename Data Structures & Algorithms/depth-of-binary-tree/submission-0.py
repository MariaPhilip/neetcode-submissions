# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        curr = root
        def count_depth(node):
            if node==None:
                return 0
            count_left = count_depth(node.left)+1
            count_right = count_depth(node.right)+1
            return max(count_left,count_right)
            
        return count_depth(curr)


    
    


        