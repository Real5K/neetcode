# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def solve(node):
            # Base case
            if node is None:
                return (0, True)  # height, is_balanced
            
            # Recurse
            left_height, left_bal = solve(node.left)
            right_height, right_bal = solve(node.right)
            
            # Combine
            current_height = max(left_height, right_height) + 1
            current_balanced = left_bal and right_bal and abs(left_height - right_height) <= 1
            
            return (current_height, current_balanced)
        
        _, result = solve(root)
        return result
        