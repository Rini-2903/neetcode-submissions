# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        return self.validInorder(root,float('-inf'),float('+inf'))
    
    def validInorder(self,root,min_val,max_val):
        if root is None:
            return True
        elif not(root.val > min_val and root.val < max_val):
            return False
        return self.validInorder(root.left,min_val,root.val) and self.validInorder(root.right,root.val,max_val)
        