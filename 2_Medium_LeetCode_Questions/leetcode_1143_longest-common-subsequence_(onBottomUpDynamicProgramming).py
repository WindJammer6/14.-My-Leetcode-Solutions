# The bottom-up dynamic programming (with tabulation) code is partially taken from my school's
# lecture notes, but I identified the recurrence that relates the sub-problems, the sub-problems
# and base cases for this question and modified the top-down dynamic programming (with tabulation)
# code to this context to answer this question

# Using an example:
# text1 = [a,b,c,d,e]
# text2 = [a,c,e]

# Let:
# - i be the index position of the letter in text1
# - j be the index position of the letter in text2
# - Each cell contains the length of the lLngest Common Subsequence (LCS) between the first i chararcters 
#   of text1 and the first j characters of text2

#             j →      0     1     2     3     4     5     
#                         (yi=a)(yi=b)(yi=c)(yi=d)(yi=e)   
#             i ↓      0     0     0     0     0     0    
#        1 (xi=a)      0     1     1     1     1     1    
#        2 (xi=c)      0     1     1     2     2     2    
#        3 (xi=e)      0     1     1     2     2     3    


# Recurrence:
# If 𝑥𝑖 = 𝑦𝑗, then 𝐷𝑃𝑙𝑒𝑛[𝑖, j] ← 𝐷𝑃𝑙𝑒𝑛[𝑖−1, 𝑗−1] + 1.
# If 𝑥𝑖 ≠ 𝑦𝑗, then 𝐷𝑃𝑙𝑒𝑛[𝑖, j] ← max{𝐷𝑃𝑙𝑒𝑛[𝑖−1, 𝑗], 𝐷𝑃𝑙𝑒𝑛[𝑖, 𝑗−1]}.

# Subproblems:
# "Compute 𝐷𝑃len[𝑖,𝑗]"" for all 1 ≤ 𝑖 ≤ 𝑚, 1 ≤ 𝑗 ≤ n

# Base cases:
# - DPlen[i,j] = 0 whenever i = 0, or j = 0

# (Note:
#  DPlen[i][j] is a dynamic programming table entry that represents:
#  - The length of the Longest Common Subsequence (LCS) between:
#  - The first i characters of text1
#  - The first j characters of text2
#  ) 

# Using bottom-up approach:
# Pseudocode:
# Initialize 2-dim array 𝐷𝑃len (with entries 𝐷𝑃len[𝑖,𝑗] for 0 ≤ 𝑖 ≤ 𝑚, 0 ≤ 𝑗 ≤ 𝑛)
# for 𝑖 from 0 to 𝑚:
#    𝐷𝑃len[𝑖,0] ← 0
# for 𝑗 from 0 to 𝑛:
#    𝐷𝑃len[0,𝑗] ← 0

# # Create the DP 2-dim array
# for 𝑖 from 1 to 𝑚:
#    for 𝑗 from 1 to 𝑛:
#        if xi == yj:                               # Case: xi = yj         
#              𝐷𝑃𝑙𝑒𝑛[𝑖, j] ← 𝐷𝑃𝑙𝑒𝑛[𝑖−1, 𝑗−1] + 1
#        else:                                      # Case: xi != yj   
#              𝐷𝑃𝑙𝑒𝑛[𝑖, j] ← max{𝐷𝑃𝑙𝑒𝑛[𝑖−1, 𝑗], 𝐷𝑃𝑙𝑒𝑛[𝑖, 𝑗−1]}

# return DP[m, n]


class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        dp = []

        # Base Cases (with the pseudocode):
        # for 𝑖 from 0 to 𝑚:
        #    𝐷𝑃len[𝑖,0] ← 0
        # for 𝑗 from 0 to 𝑛:
        #    𝐷𝑃len[0,𝑗] ← 0
        for i in range(0, len(text2) + 1):
            zeros = [0] * (len(text1) + 1)
            dp.append(zeros)

        # for row in dp:
        #     print(row)
        # print(dp[1][1])

        # Create the DP 2-dim array, and setting:
        for j in range(1, len(text1) + 1):
            for i in range(1, len(text2) + 1):

                # Case: xi = yj  
                if text1[j-1] == text2[i-1]:
                    dp[i][j] = dp[i-1][j-1] + 1

                # Case: xi != yj 
                else:
                    dp[i][j] = max(dp[i-1][j], dp[i][j-1])

        # for row in dp:
        #     print(row)

        return dp[len(text2)][len(text1)]
        

solution = Solution()
print(solution.longestCommonSubsequence("abcde", "ace"))    # 3
print(solution.longestCommonSubsequence("abc", "abc"))      # 3
print(solution.longestCommonSubsequence("abc", "def"))      # 0
print(solution.longestCommonSubsequence("bl", "yby"))       # 0
print(solution.longestCommonSubsequence("oxcpqrsvwf", "shmtulqrypy"))       # 2