# With HEAVY reference to this solution: https://www.youtube.com/watch?v=FEkZxCl_-ik (Nikhil Lohia) (YouTube video by Nikhil Lohia titled, 'Decode Ways (LeetCode 91) | Full Solution with visuals | Recursion to Dynamic Programming')

# Using top-down dynamic programming (memoization)

# Base case(s):
# (Note: 'output' is the number of ways to decode the message)
# - if index = -1 (which means when the message is empty), output = 1 (since there is only one
#   way to decode an empty message, which is to decode it as an empty group '()')


# Recurrence: 
# for any index, output = output[index - 2] (if the last 2 digits is valid (i.e. pairing of the previous index with the current index)) + output[index - 1] (if the single digit is valid (i.e. the current index itself))

# - For the last 2 digits to be valid, it needs to be between 10 - 26 (since 01 to 09 is invalid)
# - For the single digit to be valid, it needs to be between 1 - 9 (since 0 is invalid)


# Subproblems: Let dp[i] represent the number of ways to decode the substring s[0:i+1] (the first i+1 characters). Each subproblem corresponds to “How many ways are there to decode the message up to this index?”


# The top-down dynamic programming (with memoization) code is partially taken from my school's 
# lecture notes, but I identified the recurrence that relates the sub-problems, the sub-problems 
# and base cases for this question and modified the top-down dynamic programming (with memoization) 
# code to this context to answer this question

# Pseudocode:
# Using top-down dynamic programming (with memoization): 
#   Initialize memo = {} 
#   function numDecodings(m):
#   Require: m is a string of numbers
#   1. n ← len(m) - 1
#   2. key ← (m)                using the string/substring itself as the key
#   3. if key in memo then:
#   4.     return memo[key]
#   5. if m == "" then:
#   6.     memo[key] ← 1
#   7.     return 1
#   8. else: 
#   9.     result ← result[n - 2] (if the last 2 digits is valid (i.e. pairing of the previous index with the current index)) + result[n - 1] (if the single digit is valid (i.e. the current index itself))
#  10.     memo[key] ← result
#  11.     return result


class Solution:
    memo = {}       # memoization table

    def numDecodings(self, s):
        n = len(s) - 1
        if s in self.memo:             # memoization code
            return self.memo[s]        # memoization code

        if s == "":                    # Base cases
            self.memo[s] = 1           # memoization code
            # print(self.memo)
            return 1
        else:
            output = 0
            # print(n)
            # Recurrence that relates the sub-problems
            if 10 <= int(s[n-1:n+1]) <= 26:         # For the last 2 digits to be valid, it needs to be between 10 - 26 (since 01 to 09 is invalid)
                output += self.numDecodings(s[:n-1])
            
            if 1 <= int(s[n]) <= 9:                 # For the single digit to be valid, it needs to be between 1 - 9 (since 0 is invalid)
                output += self.numDecodings(s[:n])
            
            self.memo[s] = output      # memoization code
            # print(self.memo)
            return output
        

solution = Solution()
print(solution.numDecodings("12"))        # 2
print(solution.numDecodings("226"))       # 3
print(solution.numDecodings("06"))        # 0