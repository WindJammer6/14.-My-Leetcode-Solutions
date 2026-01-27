# With HEAVY reference to this solution: https://www.youtube.com/watch?v=ihj4IQGZ2zc (Neetcode) (YouTube video by Neetcode titled, 'Construct Binary Tree 
# from Inorder and Preorder Traversal - Leetcode 105 - Python')

# Pseudocode:
# 1. The first element of the preorder array is always to root node of the tree/subtree
# 2. Locate that first element aka root node of the tree/subtree in the inorder array
# 3. All elements on the left of the located first element aka root node of the 
#    tree/subtree in the inorder array is part of its left subtree, while all elements 
#    on the right is part of its right subtree
# 4. Recursively repeat this process to reconstruct the binary tree


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    # Optional method to print out the binary tree node
    def print_binary_search_tree(self, level=0):
        if self.val:
            if self.right:
                self.right.print_binary_search_tree(level + 1)

            print(' ' * 4 * level + '-> ' + str(self.val))

            if self.left:
                self.left.print_binary_search_tree(level + 1)

class Solution:
    def buildTree(self, preorder, inorder):
        root = self.buildTreeHelper(TreeNode(preorder[0]), preorder, inorder)

        return root

    def buildTreeHelper(self, root, preorder, inorder):
        if len(inorder) == 0:
            return None

        else:
            root = TreeNode(preorder[0])
            # print(f"preorder: {preorder}, preorder[0]: {preorder[0]}, inorder: {inorder}")
            # print(f"current node: {root}")
            root_index_in_inorder_array = inorder.index(preorder[0])

            # Recurse on both left and right subtrees
            left_subtree = self.buildTreeHelper(root.left, preorder[1:], inorder[:root_index_in_inorder_array])
            right_subtree = self.buildTreeHelper(root.right, preorder[1+len(inorder[:root_index_in_inorder_array]):], inorder[root_index_in_inorder_array+1:])
            
            # Combine the left and right subtrees to the root
            root.left = left_subtree
            root.right = right_subtree

            return root
        

solution = Solution()
root1 = solution.buildTree([3,9,20,15,7], [9,3,15,20,7])
root1.print_binary_search_tree()                            # [3,9,20,null,null,15,7]

root2 = solution.buildTree([-1], [-1])
root2.print_binary_search_tree()                            # [-1]

root3 = solution.buildTree([1,2], [1,2])
root3.print_binary_search_tree()                            # [1,null,2]