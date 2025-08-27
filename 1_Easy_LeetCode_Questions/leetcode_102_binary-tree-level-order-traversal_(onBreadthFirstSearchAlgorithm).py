# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def levelOrder(self, root):
        if root is None:
            return []

        result = []
        queue = []
        queue.append(root)

        while queue:
            level = [] 

            for i in range(len(queue)): 
                currentnode = queue.pop(0)
                level.append(currentnode.val)  

                if currentnode.left:
                    queue.append(currentnode.left)

                if currentnode.right:
                    queue.append(currentnode.right)

            result.append(level)

        return result


solution = Solution()
tree1 = TreeNode(3)
tree1.left = TreeNode(9)
tree1.right = TreeNode(20)
tree1.right.left = TreeNode(15)
tree1.right.right = TreeNode(7)
print(solution.levelOrder(tree1))     # [[3],[9,20],[15,7]]

tree2 = TreeNode(1)
print(solution.levelOrder(tree2))     # [[1]]