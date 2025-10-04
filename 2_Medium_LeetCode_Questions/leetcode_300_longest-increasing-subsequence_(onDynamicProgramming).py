# With HEAVY reference to this solution (Approach 1): https://leetcode.com/problems/longest-increasing-subsequence/solutions/1281811/longest-increasing-subsequence/ (Leetcode)

# This solution is just so complex... the ideas here aren't my own I'm sorry


# The bottom-up dynamic programming (with tabulation) code is partially taken from my school's
# lecture notes, but I identified the recurrence that relates the sub-problems, the sub-problems
# and base cases for this question and modified the top-down dynamic programming (with tabulation)
# code to this context to answer this question

# Using an example:
# nums = [0,1,0,3,2,3]

# Let:
# - i be the index position of the current number
# - Each cell contains the length of the longest strictly Increasing Subsequence (LIS) between the first i chararcters 

# Index i	nums[i]	 dp[i]
#    0	       0	   1
#    1	       1	   2
#    2	       0	   1
#    3	       3	   3
#    4	       2	   3
#    5	       3	   4

# - i=0: Base case - single element forms LIS of length 1
# - i=1: nums[0] < nums[1] → dp[1] = dp[0] + 1 = 2
# - i=2: No j < 2 where nums[j] < 0 → stays at base 1
# - i=3:
#   -> Check j = 0, 1, 2 → nums[1] = 1 < 3 gives best result
#   -> dp[3] = dp[1] + 1 = 3
# - i=4:
#   -> Check j = 0, 1, 2 → nums[0] = 0 < 2 and nums[2] = 0 < 2
#   -> Max from valid j's is dp[1] + 1 = 3
# - i=5:
#   -> Check j = 0, 1, 2, 3, 4 → nums[4] = 2 < 3 gives best result
#   -> dp[5] = dp[4] + 1 = 3

# Recurrence:
# dp[i] = max(dp[j] + 1) for all j where nums[j] < nums[i] and j < i

# Subproblems:
# Compute dp[i]: longest strictly Increasing Subsequence (LIS) between the first i chararcters 

# Base cases:
# - initially, dp[i] = 1 for all i from 0 to n-1 (since each individual element by itself forms an increasing subsequence of length 1. Even if no other elements can be added to it, the minimum longest increasing subsequence ending at any position i is always 1 (the element itself))

# Using bottom-up approach:
# Pseudocode:
# Initialize 1-dim array 𝐷𝑃 (with entries 𝐷𝑃[𝑖] for 0 ≤ 𝑖 ≤ 𝑛)
# for 𝑖 from 0 to n:        # Handling base case
#    if i == 0:
#        DP[i] ← 1
#    𝐷𝑃[𝑖] ← 0

# # Create the DP 1-dim array
# for 𝑖 from 1 to n:
#    for j from 0 to i:
#          if nums[i] > nums[j]:        # These next 2 lines basically handles the Recurrence (relation)
#               DP[i] = max(DP[i], DP[j] + 1)


class Solution:
    def lengthOfLIS(self, nums):

        dp = []

        # Base Cases (with the pseudocode):
        # for 𝑖 from 0 to n:        # Handling base case
        #    if i == 0:
        #        DP[i] ← 1
        #    𝐷𝑃[𝑖] ← 0
        for i in range(0, len(nums)):
            dp.append(1)

        # Create the DP 1-dim array:
        for i in range(1, len(nums)):
            for j in range(0, i):

                if nums[i] > nums[j]:
                    dp[i] = max(dp[i], dp[j] + 1)

        # print(dp)

        return max(dp)
        

solution = Solution()
print(solution.lengthOfLIS([10,9,2,5,3,7,101,18]))      # 4
print(solution.lengthOfLIS([0,1,0,3,2,3]))              # 4
print(solution.lengthOfLIS([7,7,7,7,7,7,7]))            # 1