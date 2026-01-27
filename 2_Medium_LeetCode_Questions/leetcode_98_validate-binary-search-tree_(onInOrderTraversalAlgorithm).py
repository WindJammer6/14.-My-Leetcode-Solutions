# Using the approach from this Leetcode solution using Depth First Search:
# Source:
# https://leetcode.com/problems/validate-binary-search-tree/solutions/974147/pythonjsjavagoc-on-by-dfs-and-rule-w-vis-150l/?envType=problem-list-v2&envId=oq45f3x3


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:

    is_valid_bst = True

    def isValidBST(self, root):
        # Do regular Depth First Search of a BST (doing In Order Traversal here). If a left
        # child is larger than the parent node or the right child is smaller than the parent
        # node then this tree is not a valid BST.
        self.isValidBSTHelper(root, -10000000000, 10000000000)

        return self.is_valid_bst

    def isValidBSTHelper(self, root, min, max):
        if root is not None:
            # print(min)
            # print(max)
            # print(root.val)
            if (min >= root.val) or (root.val >= max):
                self.is_valid_bst = False

            self.isValidBSTHelper(root.left, min, root.val)


            # print(min)
            # print(max)
            # print(root.val)
            if (min >= root.val) or (root.val >= max):
                self.is_valid_bst = False

            self.isValidBSTHelper(root.right, root.val, max)


solution = Solution()
tree1 = TreeNode(2)
tree1.left = TreeNode(1)
tree1.right = TreeNode(3)
print(solution.isValidBST(tree1))

solution.is_valid_bst = True

tree2 = TreeNode(5)
tree2.left = TreeNode(1)
tree2.right = TreeNode(4)
tree2.right.left = TreeNode(3)
tree2.right.right = TreeNode(6)
print(solution.isValidBST(tree2))

solution.is_valid_bst = True

tree3 = TreeNode(5)
tree3.left = TreeNode(4)
tree3.right = TreeNode(6)
tree3.right.left = TreeNode(3)
tree3.right.right = TreeNode(7)
print(solution.isValidBST(tree3))