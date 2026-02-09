# With HEAVY reference to this solution: https://www.youtube.com/watch?v=GBKI9VSKdGg (Neetcode) (YouTube video by Neetcode titled, 'Combination Sum - 
# Backtracking - Leetcode 39 - Python')


# Paseudocode (using recursion):
# 1. A regular decision tree wouldn't work since if you draw the full decision tree, you will get duplicate combinations
#    (e.g. [2, 2, 3] and [2, 3, 2])
#    Regular decision tree
#    [2, 3, 6, 7]        Target = 7

#    (root)
#    ├── 2
#    │   ├── 2
#    │   │   └── 3 -> [2, 2, 3]
#    │   └── 3
#    │       └── 2 -> [2, 3, 2]
#    ├── 3
#    ├── 6
#    │   ├── 2
#    │   ├── 3
#    │   ├── 6
#    │   └── 7
#    └── 7

#   Hence, you need to use a slightly different decision tree that prevents having these duplicate combinations like so:
#   Slightly different decision tree 
#   [2, 3, 6, 7]        Target = 7

#   (root)
#   ├── [2]
#   │   ├── [2,2]
#   │   │   ├── [2,2,2]
#   │   │   └── [2,2]
#   │   │       ├── [2,2,3]      (solution)
#   │   │       └── [2,2]
#   │   └── [2]
#   │       ├── [2,3]
#   │       └── [2]
#   ├── [3]
#   │   └── [3]
#   └── [6]
#       ├── [6]
#       └── [ ]
#           ├── [7]              (solution)
#           └── [ ]

#   where you make 2 decisions at every step, using the example above,
#   - Include current candidate (stay on same candidate list / same index)
#   - Exclude current candidate (move forward by exactly one candidate)

#   For example:
#   - in the first step, one decision is to choose at least one 2 in its combinations
#   - in the first step, the other decision is to choose no 2 at all in its combinations

#   - in the second step at the left subtree, one decision is to choose at least two 2 in its combinations
#   - in the second step at the left subtree, the other decision is to choose only one 2 in its combinations

#   etc. (watch the YouTube video for a better explanation)


# Base cases:
# - stop recursing down the slightly different decision (recursive) tree when the sum of combinations is 
#   more than the target
# - we have reached the end of the 'candidates' list


class Solution:
    def combinationSum(self, candidates, target):
        all_combinations = []
        current_node = []

        self.combinationSumHelper(current_node, candidates, target, all_combinations)

        return all_combinations
    

    def combinationSumHelper(self, current_node, candidates, target, all_combinations):

        # print(current_node)
        # print(candidates)
        

        # Base cases
        if sum(current_node) > target or len(candidates) == 0:
            return


        if sum(current_node) == target:
            all_combinations.append(current_node)
            return all_combinations


        # Recursion (the 2 decisions to make at every step in the slightly different decision (recursive) tree)
        # - Include current candidate (stay on same candidate list / same index)
        # - Exclude current candidate (move forward by exactly one candidate)
        if sum(current_node) < target:
            next_node = current_node.copy()
            next_node.append(candidates[0])
            self.combinationSumHelper(next_node, candidates, target, all_combinations)
            self.combinationSumHelper(current_node.copy(), candidates[1:], target, all_combinations)



solution = Solution()
print(solution.combinationSum([2,3,6,7], 7))        # [[2,2,3],[7]]
print(solution.combinationSum([2,3,5], 8))          # [[2,2,2,2],[2,3,3],[3,5]]
print(solution.combinationSum([2], 1))              # []