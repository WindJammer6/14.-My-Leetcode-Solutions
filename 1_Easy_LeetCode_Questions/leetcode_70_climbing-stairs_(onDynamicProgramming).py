# Question done as part of my university Algorithms module on the topic of Dynamic Programming.


# Analyzing for potential patterns for the question with trial and error: 
# Pattern i     Target value n     Total possible ways     Difference in total possible ways from previous pattern i 
#     1             1                     1                                      0
#     2             2                     2                                     +1 
#     3             3                     3                                     +1 
#     4             4                     5                                     +2 
#     5             5                     8                                     +3 
#     6             6                    13                                     +5 


# The top-down dynamic programming (with memoization) code is partially taken from my school's 
# lecture notes, but I identified the recurrence that relates the sub-problems, the sub-problems 
# and base cases for this question and modified the top-down dynamic programming (with memoization) 
# code to this context to answer this question

# Pseudocode:
# Using top-down dynamic programming (with memoization): 
# 	Initialize 𝑚𝑒𝑚𝑜 = {}  
#   function climbing_stairs(n): 
# 	Require: 𝑛 is a positive integer 
# 	1. if 𝑛 in 𝑚𝑒𝑚𝑜 then: 
#  2. 	return 𝑚𝑒𝑚𝑜[𝑛] 
# 	3. if 𝑛 == 1 then: 
# 	4. 	𝑚𝑒𝑚𝑜[𝑛] ← 1 
#  5. 	return 1 
# 	6. else if 𝑛 == 2 then: 
# 	7. 	𝑚𝑒𝑚𝑜[𝑛] ← 2 
#  8. 	return 2 
#  9. else: 
# 10. 	𝑚 ← climbing_stairs(n-1) + climbing_stairs(n-2) 
# 11. 	𝑚𝑒𝑚𝑜[𝑛] ← 𝑚 
# 12. 	return 𝑚 


class Solution:
    memo = {}                   # memoization code
    def climbStairs(self, n: int) -> int:
        if n in self.memo:      # memoization code
            return self.memo[n] # memoization code
        
        if n == 1:              # Base case 1
            self.memo[n] = 1    # memoization code
            return 1            
        elif n == 2:            # Base case 2
            self.memo[n] = 2    # memoization code
            return 2
        else:
            m = self.climbStairs(n-1) + self.climbStairs(n-2)   # Recurrence that relates the sub-problems
            self.memo[n] = m    # memoization code
            return m


solution = Solution()
print(solution.climbStairs(2))    # 2
print(solution.climbStairs(3))    # 3
print(solution.climbStairs(4))    # 4
print(solution.climbStairs(38))   # 63245986
