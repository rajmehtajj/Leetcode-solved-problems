class Solution:
    def minDepth(self, root: TreeNode) -> int:
        if not root:
            return 0
        
        if not root.left and not root.right:
            return 1
        
        if not root.left:
            return self.minDepth(root.right) + 1
        
        if not root.right:
            return self.minDepth(root.left) + 1
        
        left_depth = self.minDepth(root.left)
        right_depth = self.minDepth(root.right)
        return min(left_depth, right_depth) + 1

