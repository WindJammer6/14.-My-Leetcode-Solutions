# The bottom-up dynamic programming (with tabulation) code is partially taken from my school's
# lecture notes, but I identified the recurrence that relates the sub-problems, the sub-problems
# and base cases for this question and modified the top-down dynamic programming (with tabulation)
# code to this context to answer this question.

# With reference to the approach taken by this solution:
# Source: https://www.youtube.com/watch?v=XmSOWnL6T_I&t=302s (Pepcoding) (Youtube video by Pepcoding 
# titled 'Count Palindromic Substrings Dynamic Programming | Leetcode#647 Solution in JAVA')

# Let:
# - i be the index position of the letter in string
# - j be the index position of the letter in string
# - Each cell contains the 1 or 0, 1 representing if a substring is a palindrome from xi to yi
#   and 0 representing if a substring is not a palindrome from xi to yi

# Note: j must be larger than i for this to be valid, else we will also represent cells where
#       j is smaller than i as 0, since they are invalid

# Using an example:
# string = [b,a,b,a,d]
#             j →      0     1     2     3     4     5     
#                         (yi=b)(yi=a)(yi=b)(yi=a)(yi=d)   
#             i ↓      0     0     0     0     0     0    
#        1 (xi=b)      0     1     0     1     0     0    
#        2 (xi=a)      0     0     1     0     1     0    
#        3 (xi=b)      0     0     0     1     0     0 
#        4 (xi=a)      0     0     0     0     1     0    
#        5 (xi=d)      0     0     0     0     0     1    

# Using an example:
# string = [c,b,b,d]
#             j →      0     1     2     3     4          
#                         (yi=c)(yi=b)(yi=b)(yi=d)   
#             i ↓      0     0     0     0     0      
#        1 (xi=c)      0     1     0     0     0      
#        2 (xi=b)      0     0     1     1     0     
#        3 (xi=b)      0     0     0     1     0   
#        4 (xi=d)      0     0     0     0     1      


# Recurrence:
# - If string[i] == string[j] and DP[i+1][j-1]) = 1, then DP[i][j] = 1
#   Elaboration:
#   -> Then whether s[i..j] is a palindrome depends on inside substring s[i+1..j-1].
#   -> If s[i+1..j-1] is a palindrome (i.e., dp[i+1][j-1] == 1), then s[i..j] is also a
#      palindrome.
#   -> Otherwise, not a palindrome.

# - If string[i] != string[j], then DP[i][j] = 0
#   Elaboration:
#   -> Then immediately, s[i..j] is NOT a palindrome.


# Subproblems:
# "Compute 𝐷𝑃[𝑖,𝑗]"" for all 1 ≤ 𝑖 ≤ 𝑚, 1 ≤ 𝑗 ≤ n

# Given two indices i and j, compute whether the substring from i to j (inclusive) is a 
# palindrome. 


# Base cases:
# - if i = j, DP[i,j] = 1 (it will definiely be a palindrome)


# (Note:
#  DP[i][j] is a dynamic programming table entry that represents:
#  - The length of the Longest Palindromic Substring between:
#  - The index i and index j of string
#  ) 

# Using bottom-up approach:
# Pseudocode:
# Initialize 2-dim array 𝐷𝑃 (with entries 𝐷𝑃[𝑖,𝑗] for 0 ≤ 𝑖 ≤ 𝑚, 0 ≤ 𝑗 ≤ 𝑛)
# for 𝑖 from 0 to 𝑚:
#    𝐷𝑃[𝑖,0] ← 0
# for 𝑗 from 0 to 𝑛:
#    𝐷𝑃[0,𝑗] ← 0

# # Create the DP 2-dim array
# for 𝑖 from 1 to 𝑚:
#    for 𝑗 from 1 to 𝑛:
#        if string[i] == string[j] and DP[i+1][j-1] = True:     # Case: If string[i] == string[j] and DP[i+1][j-1] = True, then DP[i][j] = 1        
#              𝐷𝑃[𝑖, j] ← 1
#        else:                                                  # Case: string[i] != string[j], then DP[i][j] = 0
#              𝐷𝑃[𝑖, j] ← 0

# Note: If done correctly, we dont even need the 'isPalindrome' function! Dynammic Programming
#       will handle the palindrome check automatically! Very powerful!


class Solution:
    def countSubstrings(self, s: str) -> int:
        
        dp = []

        # Base Cases (with the pseudocode):
        # for 𝑖 from 0 to 𝑚:
        #    𝐷𝑃[𝑖,0] ← 0
        # for 𝑗 from 0 to 𝑛:
        #    𝐷𝑃[0,𝑗] ← 0
        for i in range(0, len(s)):
            zeros = [0] * (len(s))
            dp.append(zeros)

        for i in range(len(s)):
            dp[i][i] = 1

        # for row in dp:
        #     print(row)
        # print(dp[1][1])

        palindromic_substrings = []
        for i in s:
            palindromic_substrings.append(i)

        # Create the DP 2-dim array, and setting:
        for i in range(len(s) - 1, -1, -1):
            for j in range(i+1, len(s)):

                # Case: If string[i] == string[j] and DP[i+1][j-1] = 1, then DP[i][j] = 1      
                if (s[i] == s[j]) and (i+1 > j-1 or (dp[i+1][j-1]) == 1):
                    dp[i][j] = 1
                    palindromic_substrings.append(s[i:j+1])

                # Case: string[i] != string[j], then DP[i][j] = 0
                else:
                    dp[i][j] = 0

        # print("")
        # for row in dp:
        #     print(row)

        print(palindromic_substrings)
        
        return len(palindromic_substrings)



solution = Solution()
print(solution.countSubstrings("abc"))     # "a", "b", "c"
print(solution.countSubstrings("aaa"))     # "a", "a", "a", "aa", "aa"