# Using top-down dynamic programming

# Base case(s):
# (Note: 'output' is the number of ways to reach that particular cell)
# - if n == 1 and for any value of m, output == 1
# - if m == 1 and for any value of n, output == 1

# Recurrence: for any cells in the middle, output == output of the cell above it + output of the cell to its left

# Subproblems: Let f(i, j) represent the number of unique paths to reach cell (i, j) from (1, 1). So each subproblem corresponds to “How many ways to reach this cell?”


# The top-down dynamic programming (with memoization) code is partially taken from my school's 
# lecture notes, but I identified the recurrence that relates the sub-problems, the sub-problems 
# and base cases for this question and modified the top-down dynamic programming (with memoization) 
# code to this context to answer this question

# Pseudocode:
# Using top-down dynamic programming (with memoization): 
#   Initialize memo = {} 
#   function unique_paths(m, n):
#   Require: m and n are positive integers
#   1. key ← (m, n)
#   2. if key in memo then:
#   3.     return memo[key]
#   4. if m == 1 or n == 1 then:
#   5.     memo[key] ← 1
#   6.     return 1
#   7. else: 
#   8.     result ← unique_paths(m−1, n) + unique_paths(m, n−1)
#   9.     memo[key] ← result
#  10.     return result


class Solution:
    memo = {}       # memoization table

    def uniquePaths(self, m: int, n: int) -> int:
        if (m, n) in self.memo:             # memoization code, using tuple as dictionary key
            return self.memo[(m, n)]        # memoization code

        if n == 1 or m == 1:                # Base cases
            self.memo[(m, n)] = 1           # memoization code
            # print(self.memo)
            return 1
        else:
            output = self.uniquePaths(m - 1, n) + self.uniquePaths(m, n - 1)   # Recurrence that relates the sub-problems
            self.memo[(m, n)] = output      # memoization code
            # print(self.memo)
            return output


solution = Solution()
print(solution.uniquePaths(3, 7))       # 28
print(solution.uniquePaths(3, 2))       # 3
print(solution.uniquePaths(23, 12))     # 193536720