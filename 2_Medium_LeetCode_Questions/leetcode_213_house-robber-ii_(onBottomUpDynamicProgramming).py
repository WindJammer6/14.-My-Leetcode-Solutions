# With reference to the provided hint on Leetcode:
# """
# Since House[1] and House[n] are adjacent, they cannot be robbed together. Therefore, the problem becomes to rob either House[1]-House[n-1] or House[2]-House[n], depending on which choice offers more money. Now the problem has degenerated to the House Robber, which is already been solved.
# """

# Using an example:
# nums = [5, 3, 10, 10, 15, 7, 20]

# Let:
# index   0   1    2    3    4   5    6
# nums    5   3   10   10   15   7   20

# Compare the maximum money that can be robbed from index 0 to n - 1 VS the maximum money that can be robbed from index 1 to n. Whichever is gives the larger amount of money is the overall maximum money that can be robbed from index 0 to n.

# Then solve (find the maximum money) seperately using the same Bottom-Up Dynamic Programming approach used in the House Robber leetcode question for index 0 to n - 1 and index 1 to n before comparing the maximum money between the 2 ranges


# ////////////////////////////////////////////////////////////


# Bottom-Up Dynamic Programming approach used in the House Robber leetcode question:

# With HEAVY reference to this solution on the House Robber Leetcode question: https://www.youtube.com/watch?v=kIII1uT6F8Y (Greg Hogg) (YouTube video by Greg Hogg titled, 'House Robber - Leetcode 198 - Dynamic Programming (Python)') 

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
        # Handing edge cases
        if len(nums) == 1:
            return nums[0]

        if len(nums) == 2:
            return max(nums[0], nums[1])


        # Finding maximum amount of money that can be robbed from houses indexed 0 to n - 1
        dp1 = len(nums) * [0]

        dp1[0] = nums[0]   # Base cases
        dp1[1] = max(dp1[0], nums[1]) 

        for i in range(2, len(nums) - 1):
            dp1[i] = max(dp1[i - 2] + nums[i], dp1[i - 1])

        print(f"dp1: {dp1}")

        # Finding maximum amount of money that can be robbed from houses indexed 1 to n
        dp2 = len(nums) * [0]

        dp2[1] = nums[1]   # Base case
        dp2[2] = max(dp2[1], nums[2])    # Base case

        for i in range(3, len(nums)):
            dp2[i] = max(dp2[i - 2] + nums[i], dp2[i - 1])

        print(f"dp2: {dp2}")

        # Compare the maximum money that can be robbed from index 0 to n - 1 VS the maximum money that can be robbed from index 1 to n
        return max(dp1[-2], dp2[-1])


solution = Solution()
print(solution.rob([2,3,2]))          # 3
print(solution.rob([1,2,3,1]))        # 4
print(solution.rob([1,2,3]))          # 3