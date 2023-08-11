
class Solution:
    def getAllElements(self, root1: TreeNode, root2: TreeNode) -> List[int]:
        l=list()
        def traversal(root):
            if root is None :
                return
            l.append(root.val)
            traversal(root.left)
            traversal(root.right)
        traversal(root1)
        traversal(root2)
        l.sort()
        return l