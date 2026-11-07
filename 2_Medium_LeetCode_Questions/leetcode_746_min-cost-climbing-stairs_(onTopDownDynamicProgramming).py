# Using top-down dynamic programming (memoization)


# Using backtracking, with inspiration to the '70. Climbing Stairs' leetcode 
# question (their codes are very similar as both share a similar recurrence)


# Base case:
# - cost of the optimal way to reach end goal with index 1 is 0
# - cost of the optimal way to reach end goal with index 2 is whichever cost is lower (minimum), at 
#   index 0 or 1

# Recurrence:  
# Cost of the optimal way to reach end goal with index i depends on which is lower 
# (minimum):
# - cost of the optimal way to reach end goal with i-1 + cost at [i-1]
# - cost of the optimal way to reach end goal with i-2 + cost at [i-2]


class Solution:

    def minCostClimbingStairs(self, cost: list[int]) -> int:
        memo = {}

        return self.helper(cost, len(cost), memo)

    # i represents the end goal index 
    def helper(self, cost, i, memo):
        if i in memo:
            return memo[i]

        # Base cases
        if i == 1:
            memo[i] = 0
            return 0

        elif i == 2:
            result = min(cost[1], cost[0])
            memo[i] = result
            return result

        # Recurrence
        else:
            result = min(self.helper(cost, i-1, memo) + cost[i-1], self.helper(cost, i-2, memo) + cost[i-2])
            memo[i] = result
            return result


solution = Solution()
print(solution.minCostClimbingStairs([10,15,20]))                     # 15
print(solution.minCostClimbingStairs([1,100,1,1,1,100,1,1,100,1]))    # 6