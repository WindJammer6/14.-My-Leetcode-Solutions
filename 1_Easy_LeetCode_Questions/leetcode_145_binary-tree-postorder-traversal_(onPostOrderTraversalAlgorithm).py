# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    
    def postorderTraversal(self, root):

        list = []
        
        if root == None:
            return []

        if root.left != None:
            # Use 'extend()' function here NOT 'append()'!
            list.extend(self.postorderTraversal(root.left))

        if root.right != None:
            # Use 'extend()' function here NOT 'append()'!
            list.extend(self.postorderTraversal(root.right))
            
        list.append(root.val)

        return list
    
    # Why use 'extend()' function here NOT 'append()'?
    # append vs extend | Meaning
    # .append(list)    | Adds the whole list as one element (nested list)
    # .extend(list)    | Adds each element inside the list to your list (flat)

    # If you use 'append()' function the output will be:
    # Output:
    # [1, [[3], 2]]
    # [[[4], 2, [[6], 5, [7]]], 1, [3, [[9], 8]]]
    # [1]

    # Only if you use 'extend()' function the output will be:
    # Output:
    # [1, 3, 2]
    # [4, 2, 6, 5, 7, 1, 3, 9, 8]
    # [1]


solution = Solution()
tree1 = TreeNode(1)
tree1.right = TreeNode(2)
tree1.right.left = TreeNode(3)
print(solution.inorderTraversal(tree1))

tree2 = TreeNode(1)
tree2.left = TreeNode(2)
tree2.right = TreeNode(3)

tree2.left.left = TreeNode(4)
tree2.left.right = TreeNode(5)
tree2.left.right.left = TreeNode(6)
tree2.left.right.right = TreeNode(7)

tree2.right.right = TreeNode(8)
tree2.right.right.left = TreeNode(9)

print(solution.inorderTraversal(tree2))

tree3 = TreeNode(1)
print(solution.inorderTraversal(tree3))