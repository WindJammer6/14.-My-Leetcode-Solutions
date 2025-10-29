# With HEAVY reference to this solution: https://leetcode.com/problems/coin-change-ii/solutions/3892702/100-dynamic-programming-video-optimal-solution/?envType=problem-list-v2&envId=oq45f3x3 (vanAmsen on Leetcode)

# This solution is just so complex... the ideas here aren't my own I'm sorry

# Additional sources I tried studying with:
# - https://www.youtube.com/watch?v=7V3FiGBEThg&t=271s (vanAmsen) (YouTube tutorial by vanAmsen titled, 'Master the LeetCode 518. Coin Change II in Python | Dynamic Programming Deep Dive')
# - https://www.youtube.com/watch?v=g0VjciqYeDU&list=PLVrpF4r7WIhTT1hJqZmjP10nxsmrbRvlf&index=15 (Andrey Grehov) (YouTube tutorial by Andrey Grehov titled, '15. Coin Change. Unique Ways. (Dynamic Programming for Beginners)')


# The bottom-up dynamic programming (with tabulation) code is partially taken from my school's
# lecture notes, but I identified the recurrence that relates the sub-problems, the sub-problems
# and base cases for this question and modified the top-down dynamic programming (with tabulation)
# code to this context to answer this question

# Analyzing for potential patterns for the question with trial and error: 
# amount = 5, coins = [1,2,5]

# 1 -> try 1 (YES) -> try 1 (YES) -> try 1 (YES) ... etc.
#                                 -> try 2 (YES)
#                                 -> try 5 (NO)
#                  -> try 2 (YES) -> try 1 (YES)
#                                 -> try 2 (YES)
#                                 -> try 5 (NO)
#                  -> try 5 (NO)  


#   -> try 2 (YES) -> try 1 (YES) -> try 1 (YES)
#                                 -> try 2 (YES)
#                                 -> try 5 (NO)
#                  -> try 2 (YES) -> try 1 (YES)
#                                 -> try 2 (NO)
#                                 -> try 5 (NO)
#                  -> try 5 (NO)  


# Using an example:
# amount = 5, coins = [1,2,5]

# Let:
# - j be amount to meet
# - Each cell contains number of ways to meet that amount

#      Amount     	0	1	2	3	4	5
#      Initial	    1	0	0	0	0	0
#      Coin 1	    1	1	1	1	1	1   (using only coin 1s)
#      Coin 2	    1	1	2	2	3	3   (using coin 1s and 2s) (add up from previous row)
#      Coin 5	    1	1	2	2	3	4   (using coin 1s, 2s and 5s) (add up from previous row)

# Looking at the last row of the table, we can infer its recurrence. Assume that the last row is simply a 1D-array 'dp'

# Recurrence:
# dp[i] = dp[i] + dp[i - coin_value]

# Subproblems:
# Compute dp[i]: number of distinct ways to form a specific, smaller amount i, using only the coins we have processed so far

# Base cases:
# - dp[0] = 1 (since there is only 1 way to get amount = 0, which is to pick nothing)

class Solution:
    def change(self, amount, coins):
        dp = [1] + [0] * (amount)     # bottom-up tabulation array
        print(dp)

        for i in range(len(coins)):
            for j in range(coins[i], amount + 1):
                dp[j] = dp[j] + dp[j - coins[i]]

        print(dp)

        return dp[amount]

            
solution = Solution()
print(solution.change(5, [1,2,5]))      # 4
print(solution.change(3, [2]))          # 0
print(solution.change(10, [10]))        # 1