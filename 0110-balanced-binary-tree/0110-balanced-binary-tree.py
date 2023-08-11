class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def height(node):
            if not node:
                return 0
            left_height = height(node.left)
            right_height = height(node.right)
            return max(left_height, right_height) + 1
        
        def is_balanced_helper(node):
            if not node:
                return True
            left_height = height(node.left)
            right_height = height(node.right)
            if abs(left_height - right_height) > 1:
                return False
            return is_balanced_helper(node.left) and is_balanced_helper(node.right)
        return is_balanced_helper(root)
