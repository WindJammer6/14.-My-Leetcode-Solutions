# Using bottom-up dynamic programming

# Base case: the last element is always a good index

# Recurrence: If there is a good index within the range to the right specified by the 
# value at that index, then, that index is a good index, else, it is a bad index

# Subproblems: Each subproblem dp[i] depends only on the subproblems to its right (dp[i+1] ... dp[i+nums[i]]), which have already been solved when we process i in reverse order.

# For example:
#   Index  0  1  2  3  4  5  6
#   nums   2  4  2  1  0  2  0
#   memo   G  G  B  B  B  G  G

# where "G" means good index and "B" means bad index


# From the Leetcode solution, https://leetcode.com/problems/jump-game/solutions/127838/jump-game/ (Leetcode):
# Naming:
# We call a position in the array a "good index" if starting at that position, we can 
# reach the last index. Otherwise, that index is called a "bad index". The problem 
# then reduces to whether or not index 0 is a "good index".

class Solution:
    def canJump(self, nums):
        dp = []
        for i in range(len(nums) - 1):
            dp.append(0)
        dp.append(1)                # base case: the last element is always a good index
        print(dp)

        for i in range(len(nums) - 1, -1, -1):
            print(f"Current Index: {i}")

            # Recurrence
            print(f"i: {i}")
            print(f"i + nums[i]: {i + nums[i] + 1}")
            print(dp[i : i + nums[i] + 1])
            if 1 in dp[i : i + nums[i] + 1]:
                dp[i] = 1

        print(dp)

        if dp[0] == 1:
            return True
        else:
            return False
        

solution = Solution()
print(solution.canJump([2,3,1,1,4]))        # True
print(solution.canJump([3,2,1,0,4]))        # False