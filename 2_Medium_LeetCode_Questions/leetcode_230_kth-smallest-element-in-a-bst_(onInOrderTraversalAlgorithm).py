# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def kthSmallest(self, root, k):
        list = []
        self.kthSmallestHelper(root, list)

        # print(list)
        return list[k-1]

    def kthSmallestHelper(self, root, list):
        if root is not None:
            self.kthSmallestHelper(root.left, list)
            # print(root.val)
            list.append(root.val)
            self.kthSmallestHelper(root.right, list)


solution = Solution()
tree1 = TreeNode(3)
tree1.left = TreeNode(1)
tree1.right = TreeNode(4)
tree1.left.right = TreeNode(2)
print(solution.kthSmallest(tree1, 1))       # 1

tree2 = TreeNode(5)
tree2.left = TreeNode(3)
tree2.right = TreeNode(6)
tree2.left.left = TreeNode(2)
tree2.left.right = TreeNode(4)
tree2.left.left.left = TreeNode(1)
print(solution.kthSmallest(tree2, 3))       # 3

tree3 = TreeNode(4)
tree3.left = TreeNode(2)
tree3.right = TreeNode(5)
tree3.left.right = TreeNode(3)
print(solution.kthSmallest(tree3, 1))       # 2