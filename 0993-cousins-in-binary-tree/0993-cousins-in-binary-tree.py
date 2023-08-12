class Solution:
    def isCousins(self, root: Optional[TreeNode], x: int, y: int) -> bool:
        def dfs(node, parent, depth, target):
            if not node:
                return
            
            if node.val == target:
                return (parent, depth)
            
            return dfs(node.left, node, depth + 1, target) or dfs(node.right, node, depth + 1, target)
        
        x_parent, x_depth = dfs(root, None, 0, x)
        y_parent, y_depth = dfs(root, None, 0, y)
        
        return x_depth == y_depth and x_parent != y_parent
