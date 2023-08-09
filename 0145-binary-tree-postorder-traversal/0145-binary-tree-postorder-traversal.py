
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

