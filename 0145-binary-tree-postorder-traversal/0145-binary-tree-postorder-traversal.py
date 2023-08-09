class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        result = []
        self._postorderTraversal(root, result)
        return result
    
    def _postorderTraversal(self, node, result):
        if node:
            self._postorderTraversal(node.left, result)
            self._postorderTraversal(node.right, result)
            result.append(node.val)

