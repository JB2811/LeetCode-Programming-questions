# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    l=[]
    def postorder(self, root: Optional[TreeNode]) -> List[int]:
     if(root!=None):
      self.postorder(root.left)
      self.postorder(root.right)
      self.l.append(root.val)
     return self.l
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
     self.l=[]
     return self.postorder(root)