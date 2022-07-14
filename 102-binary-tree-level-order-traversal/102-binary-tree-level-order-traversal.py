# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        levelNodes = []
        def levelOrderRecursive(root: Optional[TreeNode], depth: int) -> None:
            if not root: return
            
            nonlocal levelNodes
            
            if len(levelNodes) <= depth: 
                levelNodes.append([root.val])
            else: 
                levelNodes[depth].append(root.val)   
            levelOrderRecursive(root.left, depth+1)  
            levelOrderRecursive(root.right, depth+1)                             
        
        levelOrderRecursive(root, 0)
        return levelNodes      