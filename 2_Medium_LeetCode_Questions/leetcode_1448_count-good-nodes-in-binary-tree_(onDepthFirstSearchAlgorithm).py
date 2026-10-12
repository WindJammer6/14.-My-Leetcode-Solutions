# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:

    # Approach 1 (my own, works): Path list as tracker of max value seen so far in path
    # def dfs(self, root, path):
    #     count = 0

    #     if root is None:
    #         return 0
        
    #     path.append(root.val)
    #     # print(path)
    #     # print(root.val)
    #     if max(path) <= root.val:
    #         count += 1
        
    #     left_count = self.dfs(root.left, path)
    #     right_count = self.dfs(root.right, path)

    #     path.pop()

    #     return count + left_count + right_count
    

    # Approach 2 (recommended by Neetcode at https://www.youtube.com/watch?v=qB0zZpBJlh8 
    # (Neetcode) (YouTube video by Neetcode titled, 'Microsoft's Most Asked Question 2021 - 
    # Count Good Nodes in a Binary Tree - Leetcode 1448 - Python'), works): Parameter as 
    # tracker of max value seen so far in path
    def dfs(self, root, path, max):
        count = 0

        if root is None:
            return 0
        
        path.append(root.val)
        # print(path)
        # print(root.val)
        if max <= root.val:
            max = root.val
            count += 1
        
        left_count = self.dfs(root.left, path, max)
        right_count = self.dfs(root.right, path, max)

        return count + left_count + right_count

    def goodNodes(self, root):
        count = self.dfs(root, [], root.val)
        return count



solution = Solution()

# Test Case 1: [3,1,4,3,null,1,5]
root1 = TreeNode(3)
root1.left = TreeNode(1)
root1.right = TreeNode(4)
root1.left.left = TreeNode(3)
root1.right.left = TreeNode(1)
root1.right.right = TreeNode(5)
print(solution.goodNodes(root1))    # 4


# Test Case 2: [3,3,null,4,2]
root2 = TreeNode(3)
root2.left = TreeNode(3)
root2.left.left = TreeNode(4)
root2.left.right = TreeNode(2)
print(solution.goodNodes(root2))    # 3


# Test Case 3: [1]
root3 = TreeNode(1)
print(solution.goodNodes(root3))    # 1


# Test Case 4: [2,null,4,10,8,null,null,4]
root4 = TreeNode(2)
root4.right = TreeNode(4)
root4.right.left = TreeNode(10)
root4.right.right = TreeNode(8)
root4.right.left.left = TreeNode(4)
print(solution.goodNodes(root4))    # 4