# With HEAVY reference to this solution from the Leetcode discussion section by Ivan Stebletsov:
# """
# Refreshing my knowledge about key traits of binary search tree very helped me find simple solution for this 
# problem. I'd recommend you start from it.

# BST has following traits:
# 1. Both root's subtrees also are binary (it is not important for solution, but just FYI);
# 2. All LEFT child nodes of LEFT subtree have values less or equal the value of the current node.
# 3. All RIGHT child nodes of RIGHT subtree have values greater the value of the current node.

# Keeping in mind these traits we can start traverse tree in depth (DFS).
# Main idea:
# - If current node value > p.value and q.value, hence according to trait №2 above, it's useless search common node 
#   for p and q in the right subtree -> continue traverse next node in left subtree.
# - If current node value < p.value and q.value, hence according to trait №3 above, it's useless search common node 
#   for p and q in the left subtree -> continue traverse next node in right subtree
# - If according to statements above it's useless search common node in both left and right subtree, it means that 
#   you are in a right place, you have found Lowest Common Ancestor.

# Using this idea you can solve problem both iteratively and recursively.

# If I'm not mistaken time complexity will be O(logN), because every time we chose only one subtree, therefore 
# reduce count of traversable nodes twice. Memory complexity O(1).

# Hope it will be helpful.
# """



# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def lowestCommonAncestor(self, root, p, q):
        if root is not None:
            # print(root.val)
            if root.val > p.val and root.val > q.val:       
                return self.lowestCommonAncestor(root.left, p, q)
            
            if root.val < p.val and root.val < q.val:
                return self.lowestCommonAncestor(root.right, p, q)

            # Deciding which node is the smaller node
            if p.val > q.val:
                if (root.val >= q.val) and (root.val <= p.val):
                    return root

            else:
                # print(f"p: {p.val} q: {q.val}, root: {root.val}")
                if (root.val >= p.val) and (root.val <= q.val):
                    return root
       

solution = Solution()
tree1 = TreeNode(6)
tree1.left = TreeNode(2)
tree1.right = TreeNode(8)
tree1.left.left = TreeNode(0)
tree1.left.right = TreeNode(4)
tree1.left.right.left = TreeNode(3)
tree1.left.right.right = TreeNode(5)
tree1.right.left = TreeNode(7)
tree1.right.right = TreeNode(9)
print(solution.lowestCommonAncestor(tree1, TreeNode(2), TreeNode(8)).val)       # 6

tree2 = TreeNode(6)
tree2.left = TreeNode(2)
tree2.right = TreeNode(8)
tree2.left.left = TreeNode(0)
tree2.left.right = TreeNode(4)
tree2.left.right.left = TreeNode(3)
tree2.left.right.right = TreeNode(5)
tree2.right.left = TreeNode(7)
tree2.right.right = TreeNode(9)
print(solution.lowestCommonAncestor(tree2, TreeNode(2), TreeNode(4)).val)       # 2

tree3 = TreeNode(2)
tree3.left = TreeNode(1)
print(solution.lowestCommonAncestor(tree3, TreeNode(2), TreeNode(1)).val)       # 2