# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        
        result_list = []
        
        if root != None: 
        
            if root.left:
                left = self.inorderTraversal(root.left)
                result_list += left

            result_list.append(root.val)

            if root.right:
                right = self.inorderTraversal(root.right)
                result_list += right
        
        return result_list
        
        
        
#         if root == None:
#             return []
        
#         result_list = [root.val]
#         i = result_list.index(root.val)

#         while (root.left != None) or (root.right != None):
#             if root.left == None:
#                 result_list.insert((i+1), root.right.val)
#                 i = result_list.index(root.right.val)
#                 root = root.right
                
#             elif root.right == None:
#                 result_list.insert(i, root.left.val)
#                 i = result_list.index(root.left.val)
#                 root = root.left
                
                
#         return result_list