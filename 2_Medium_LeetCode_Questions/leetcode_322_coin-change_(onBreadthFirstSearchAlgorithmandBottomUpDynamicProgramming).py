# With reference to this solution: https://leetcode.com/problems/coin-change/?envType=problem-list-v2&envId=oizxjoit (Hieroglyphs on Leetcode)

# Using an example:
# amount = 5, coins = [1,2,5]

# Levels  0               1              2
#        11 - minus 1 -> 10 - minus 1 -> 9 (Prune this branch) ... etc.
#                           - minus 2 -> 8 
#                           - minus 5 -> 5

#           - minus 2 -> 9  - minus 1 -> 8 (Prune this branch)
#                           - minus 2 -> 7
#                           - minus 5 -> 4

#           - minus 5 -> 6  - minus 1 -> 5
#                           - minus 2 -> 4 (Prune this branch)
#                           - minus 5 -> 1

# - We can draw a General Tree Data Structure using this logic
# - We can discard duplicate nodes and prune its branch that have been seen before
# - Fewest levels to reach 0 -> Fewest number of coins required


# Approach 1: Using Breadth First Search (BFS) (works) 
from collections import deque

class Solution:
    def coinChange(self, coins, amount):
        queue = deque()     # using deque instead of lists because doing '.pop(0)' is O(n) with 
                            # normal lists, which caused some test cases to give Time Limit 
                            # Exceeded (TLE), while doing '.popleft()' is O(1) with deque
        # queue = []
        visited = set()     # using set instead of lists since doing an 'in' operator is O(n) 
                            # with normal lists, which caused some test cases to give Time Limit 
                            # Exceeded (TLE), while doing 'in' operator is O(1) with set
        # visited = []      # for pruning

        queue.append((amount, 0))

        while queue:
            # current_node = queue.pop(0)
            current_node = queue.popleft()
            # print(queue)
            # print(current_node[0])

            if current_node[0] == 0:
                return current_node[1]

            for coin in coins:
                new_node = current_node[0] - coin
                if new_node >= 0 and new_node not in visited:
                    queue.append((new_node, current_node[1] + 1))
                    visited.add(new_node)

        return -1


solution = Solution()
print(solution.coinChange([1,2,5], 11))     # 3
print(solution.coinChange([2], 3))          # -1
print(solution.coinChange([1], 0))          # 0


# ///////////////////////////////////////////////////////////


# With HEAVY reference to this solution: https://www.youtube.com/watch?v=H9bfqozjoqs (Neetcode) (YouTube video 
# by Neetcode titled "Coin Change - Dynamic Programming Bottom Up - Leetcode 322")


# The bottom-up dynamic programming (with tabulation) code is partially taken from my school's
# lecture notes, but I identified the recurrence that relates the sub-problems, the sub-problems
# and base cases for this question and modified the top-down dynamic programming (with tabulation)
# code to this context to answer this question

# Using an example:
# amount = 5, coins = [1,2,5]
# The index of 'dp' represent the amount remaining to make up the full amount

# With amount 0 -> can't use 1 coin
#               -> can't use 2 coin
#               -> can't use 5 coin
# (minimum number of coins for 'dp[0]' i.e. amount 0, is 0)

# With amount 1 -> use 1 coin       -> one, 1 coin + dp[0] -> 1 + 0
#               -> can't use 2 coin
#               -> can't use 5 coin 
# (minimum number of coins for 'dp[1]' i.e. amount 1, is 1)

# With amount 2 -> can use 1 coin   -> one, 1 coin + dp[1] -> 1 + 1 
#               -> can't use 2 coin -> one, 2 coin + dp[0] -> 1 + 0
#               -> can't use 5 coin 
# (minimum number of coins for 'dp[2]' i.e. amount 2, is 1)

# With amount 3 -> can't use 1 coin -> one, 1 coin + dp[2] -> 1 + 2
#               -> can't use 2 coin -> one, 2 coin + dp[1] -> 1 + 1
#               -> can't use 5 coin 
# (minimum number of coins for 'dp[3]' i.e. amount 3, is 2)

# etc.


# Recurrence:
# dp[i] = min(dp[i], dp[i - coin_value] + 1)

# Subproblems:
# Compute dp[i]: For each amount i from 0 to amount, compute dp[i] as the minimum coins required to reach i, by considering each
#                coin value (only 1 each) to be used and combining it with the optimal solution for the remaining amount i - coin value.

# Base cases:
# - dp[0] = 0 (0 coins needed to make amount 0)


# Approach 2: Bottom-Up Dynamic Programming (works) 
class Solution:
    def coinChange(self, coins, amount):
        dp = [-1] * (amount + 1)    
        
        dp[0] = 0 # Base case

        for i in range(1, amount + 1):
            list_to_find_min = []
            for coin in coins:
                if coin <= i and dp[i - coin] != -1:        # need this 'dp[i - coin] != -1' to check if it is an impossible state
                    list_to_find_min.append(1 + dp[i - coin])

            # print(dp)
            # print(list_to_find_min)

            if len(list_to_find_min) == 0:
                pass
            else:
                dp[i] = min(list_to_find_min)

        return dp[amount]
                


solution = Solution()
print(solution.coinChange([1,2,5], 11))     # 3
print(solution.coinChange([2], 3))          # -1
print(solution.coinChange([1], 0))          # 0