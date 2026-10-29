# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        ans = []
        self.check(root,0,ans)
        return ans
    
    def check(self,root,level,ans):
        if root is None:
            return 
        if level == len(ans):
            ans.append(root.val)
        self.check(root.right,level+1,ans)
        self.check(root.left,level+1,ans)
        return ans

        