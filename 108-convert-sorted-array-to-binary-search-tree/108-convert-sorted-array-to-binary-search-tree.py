# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        if not nums: return None  
        # <-- base case: leaf
        mid = len(nums)//2
        # create new tree with root equals to the mid point and the lift branch is
        # the list on the lift and the right be the tree on the right. 
        # example [-10,-3,0,5,9] -->      0
        #                              /     \
        #                           [-10,-3]     [5,9] 
        # then find the mid for the new list which is one in the 2 cases 
        #   the new root will be  -3,              9  
        #                        /   \           /   \
        #                     -10   NULL        5    null
        
        return TreeNode(nums[mid],self.sortedArrayToBST(nums[:mid]),
                             self.sortedArrayToBST(nums[mid+1:]))