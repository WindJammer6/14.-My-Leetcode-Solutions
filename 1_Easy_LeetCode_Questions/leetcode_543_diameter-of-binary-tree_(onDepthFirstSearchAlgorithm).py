# With HEAVY reference to this solution: https://www.youtube.com/watch?v=K81C31ytOZE (NeetcodeIO) (YouTube video by NeetcodeIO titled, 
# 'Diameter of Binary Tree - Leetcode 543 - Python') (particularly the idea to use a global variable to
# track the diameter of every node)


# Pseudocode:
# 1. Diameter of any binary tree is the height of longest path of left subtree + height of longest path
#    of right subtree 
#    (Note: height = longest downward path from a node to a leaf)
# 2. We need to track the diameter from every node in the binary tree, and the diameter of the entire 
#    binary tree is the diameter of the node with the largest/maximum diameter. We will be tracking the
#    diameter of every node in a global variable.
# 3. Before this, we need to not only track the diameter of every node in the binary tree, but also its
#    height, which can be calculated by taking:
#       max(height of the left subtree, height of the right subtree) + 1

#    We will be tracking the height of every node by returning it in our recursive Depth First Search 
#    (DFS) algorithm


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    diameter = 0

    def dfs(self, root):
        if root is None:
            return 0

        height_of_left_subtree = self.dfs(root.left)
        height_of_right_subtree = self.dfs(root.right)
        if height_of_left_subtree + height_of_right_subtree > self.diameter:
            self.diameter = height_of_left_subtree + height_of_right_subtree
        height = max(height_of_left_subtree, height_of_right_subtree) + 1

        # print(height)
        return height

    def diameterOfBinaryTree(self, root):
        self.dfs(root)
        return self.diameter


solution = Solution()

root1 = TreeNode(1)
root1.left = TreeNode(2)
root1.right = TreeNode(3)
root1.left.left = TreeNode(4)
root1.left.right = TreeNode(5)
print(solution.diameterOfBinaryTree(root1))  # 3

solution.diameter = 0

root2 = TreeNode(1)
root2.left = TreeNode(2)
print(solution.diameterOfBinaryTree(root2))  # 1