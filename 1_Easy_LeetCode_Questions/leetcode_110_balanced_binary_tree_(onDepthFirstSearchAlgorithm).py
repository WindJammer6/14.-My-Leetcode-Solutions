# With inspiration to the '543. Diameter of Binary Tree' leetcode 
# question (their codes are very similar as both uses a global variable to track the objective and uses
# height of a binary tree to determine the objective, tracked by returning it during the recursive
# Depth First Search (DFS) algorithm)


# Pseudocode:
# 1. Do Depth First Search (DFS) algorithm and track/calculate the height of the left and right subtree 
#    for every node via returning the height.
# 2. The height at every node can be calculated by:
#       max(height_of_left_subtree, height_of_right_subtree) + 1
# 3. If the height of the left and right subtree for a node differs more than 1, then return false,
#    that the binary tree is not height balanced. Else, return true, that the binary tree is height 
#    balanced. We track whether at every node if it is height balanced via a global variable.


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    height_balanced = True

    def dfs(self, root):
        if root is None:
            return 0

        height_of_left_subtree = self.dfs(root.left)
        height_of_right_subtree = self.dfs(root.right)
        if abs(height_of_left_subtree - height_of_right_subtree) > 1:
             self.height_balanced = False
        height = max(height_of_left_subtree, height_of_right_subtree) + 1

        # print(height)
        return height

    def isBalanced(self, root: TreeNode | None) -> bool:
        self.dfs(root)
        return self.height_balanced


solution = Solution()

root1 = TreeNode(3)
root1.left = TreeNode(9)
root1.right = TreeNode(20)
root1.right.left = TreeNode(15)
root1.right.right = TreeNode(7)
print(solution.isBalanced(root1))  # True

solution.height_balanced = True

root2 = TreeNode(1)
root2.left = TreeNode(2)
root2.right = TreeNode(2)
root2.left.left = TreeNode(3)
root2.left.right = TreeNode(3)
root2.left.left.left = TreeNode(4)
root2.left.left.right = TreeNode(4)
print(solution.isBalanced(root2))  # False

solution.height_balanced = True

root3 = None
print(solution.isBalanced(root3))  # True