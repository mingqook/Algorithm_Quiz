# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
   
        
class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        if root == None:
            return True
        
        def same_check(left, right):
            
            if left == None and right == None:
                return True
            elif left == None and right != None:
                return False
            elif left != None and right == None:
                return False
            elif left.val != right.val:
                return False
            
            return same_check(left.left, right.right) and same_check(left.right, right.left)
            
        return same_check(root.left, root.right)