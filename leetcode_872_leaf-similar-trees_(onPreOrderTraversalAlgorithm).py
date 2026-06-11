# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def preorderdfs(self, root, seq):
        if root is None:
            return None
        
        print(root.val)
        if (root.left is None) and (root.right is None):
            print(f"Found leaf node: {root.val}")
            seq.append(root.val)

        self.preorderdfs(root.left, seq)
        self.preorderdfs(root.right, seq)

        return seq

    def leafSimilar(self, root1, root2):
        seq1 = []
        seq2 = []

        self.preorderdfs(root1, seq1)
        print(seq1)

        self.preorderdfs(root2, seq2)
        print(seq2)
        
        return (seq1 == seq2)


solution = Solution()

root1 = TreeNode(3)
root1.left = TreeNode(5)
root1.left.left = TreeNode(6)
root1.left.right = TreeNode(2)
root1.left.right.left = TreeNode(7)
root1.left.right.right = TreeNode(4)
root1.right = TreeNode(1)
root1.right.left = TreeNode(9)
root1.right.right = TreeNode(8)

root2 = TreeNode(3)
root2.left = TreeNode(5)
root2.left.left = TreeNode(6)
root2.left.right = TreeNode(7)
root2.right = TreeNode(1)
root2.right.left = TreeNode(4)
root2.right.right = TreeNode(2)
root2.right.right.left = TreeNode(9)
root2.right.right.right = TreeNode(8)

print(solution.leafSimilar(root1, root2))      # True


root3 = TreeNode(1)
root3.left = TreeNode(2)
root3.right = TreeNode(3)

root4 = TreeNode(1)
root4.left = TreeNode(3)
root4.right = TreeNode(2)

print(solution.leafSimilar(root3, root4))      # False