
class Solution:
    def getMinimumDifference(self, root: Optional[TreeNode]) -> int:
        prev = float('-inf')
        min_diff = float('inf')
        
        def inorderTraversal(root):
            nonlocal prev, min_diff
            if not root:
                return
            if root.left:
                inorderTraversal(root.left)
            if (root.val - prev) < min_diff:
                min_diff = root.val - prev
            prev = root.val
            if root.right:
                inorderTraversal(root.right)
                
        inorderTraversal(root)
        return min_diff