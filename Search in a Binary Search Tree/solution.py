# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def searchBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        ans=None
        def traverse(root):
            nonlocal ans
            if ans or not root:
                return
            if root.val<val:
                traverse(root.right)
            elif root.val>val:
                traverse(root.left)
            else:
                ans=root
                return

        traverse(root)
        return ans
