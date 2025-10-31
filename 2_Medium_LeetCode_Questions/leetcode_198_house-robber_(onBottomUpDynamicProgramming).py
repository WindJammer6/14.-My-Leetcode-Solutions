# With HEAVY reference to this solution: https://www.youtube.com/watch?v=kIII1uT6F8Y (Greg Hogg) (YouTube video by Greg Hogg titled, 'House Robber - Leetcode 198 - Dynamic Programming (Python)')

# Using an example:
# nums = [5, 3, 10, 10, 15, 7, 20]

# Let:
# index   0   1    2    3    4   5    6
# nums    5   3   10   10   15   7   20

# dp      5                                (maximum money can rob at index 0)
#   -> choose to rob first house
# dp      5   5                            (maximum money can rob from index 0 to 1)
#   -> choose not to rob second house
# dp      5   5   15                       (maximum money can rob from index 0 to 2)
#   -> choose to rob third house
# dp      5   5   15   15                  (maximum money can rob from index 0 to 3)
#   -> both cases if you choose to rob fourth house or not will similarly give you maximum money 
#      you can rob of 15
# dp      5   5   15   15   30             (maximum money can rob from index 0 to 4)
#   -> choose to rob fifth house
# dp      5   5   15   15   30  30         (maximum money can rob from index 0 to 4)
#   -> choose not to rob the sixth house (if you choose to rob it the maximum money you can rob is 
#      22, but you are better off not robbing it since by doing so the maximum money you can rob 
#      is 30 instead!)
# dp      5   5   15   15   30  30   50    (maximum money can rob from index 0 to 4)
#   -> choose to rob the seventh house

# (the 'dp' table stores the maximum money you can rob at from 0 to that index)


# Recurrence:
# For every next house you visit, you can choose either to rob it, or not rob it. 
# - If you choose to rob it, then you add the amount of money at that house plus the maximum 
#   money you can rob from 2 houses back
# - Else, if you choose not to rob it, you don't then you add the amount of money at that house 
#   plus the maximum money you can rob from 1 house back

# Then, pick the choice (to rob the current house, or to not rob the current house) that will give 
# you the maximum money you can rob

# Subproblems:
# Compute dp[i]: maximum amount of money that can be robbed from houses 0 to i

# Base cases:
# - at dp[0], then choose rob that first house (dp[0] = nums[0])
# - at dp[1], 
#   -> if nums[1] > nums[0], then choose to rob the second house instead of the first (dp[1] = nums
#      [1])
#   -> else if nums[1] < nums[0], then choose to rob the first house instead of the second (dp[1] = nums[0])


class Solution:
    def rob(self, nums):
        dp = [0] * len(nums)            # bottom-up tabulation array
        
        dp[0] = nums[0]                 # Base case
        print(dp)

        for i in range(1, len(nums)):
            if i == 1:                  # Base case
                if nums[1] > nums[0]:
                    dp[1] = nums[1]
                else:
                    dp[1] = dp[0]             
            else:
                dp[i] = max(dp[i - 1], dp[i - 2] + nums[i])

        print(dp)

        return max(dp[len(nums) - 1], dp[len(nums) - 2])
            

solution = Solution()
print(solution.rob([1,2,3,1]))          # 4
print(solution.rob([2,7,9,3,1]))        # 12
print(solution.rob([1,3,1,3,100]))      # 103