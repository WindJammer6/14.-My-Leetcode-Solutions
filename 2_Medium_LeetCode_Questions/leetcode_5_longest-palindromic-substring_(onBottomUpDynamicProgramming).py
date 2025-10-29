# Approach 1: Brute force approach (dosen't work, exceeds time limit)
class Solution:
    # Using two pointers
    def isPalindrome(self, s):
        left = 0
        right = len(s) - 1
        while right > left:
            if s[left] != s[right]:
                return False
            
            right -= 1
            left += 1

        return True
    

    def longestPalindrome1(self, s: str) -> str:

        longest_palindromic_substring = ""
        right = 0

        for i in range(len(s)):

            for j in range(i, len(s)+1):
                right = j
                substring = s[i:right]
                # print(self.isPalindrome(substring))

                if (self.isPalindrome(substring) == True):
                    if (len(substring) > len(longest_palindromic_substring)):
                        longest_palindromic_substring = substring

        return longest_palindromic_substring


    # ///////////////////////////////////////////////////////////////////////////////


    # The bottom-up dynamic programming (with tabulation) code is partially taken from my school's
    # lecture notes, but I identified the recurrence that relates the sub-problems, the sub-problems
    # and base cases for this question and modified the top-down dynamic programming (with tabulation)
    # code to this context to answer this question.

    # With reference to the approach taken by this solution:
    # Source: https://www.youtube.com/watch?v=UflHuQj6MVA&t=642s (Techdose) (Youtube video by Techdose 
    # titled 'Longest palindromic substring | Dynamic programming')

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


    # Approach 2: Using Dynammic Programming
    def longestPalindrome2(self, s: str) -> str:

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

        for row in dp:
            print(row)
        # print(dp[1][1])

        # Create the DP 2-dim array, and setting:
        longest_palindromic_substring = s[0]
        for i in range(len(s) - 1, -1, -1):
            for j in range(i+1, len(s)):

                # Case: If string[i] == string[j] and DP[i+1][j-1] = 1, then DP[i][j] = 1      
                if (s[i] == s[j]) and (i+1 > j-1 or (dp[i+1][j-1]) == 1):
                    dp[i][j] = 1
                    if j + 1 - i > len(longest_palindromic_substring):
                        longest_palindromic_substring = s[i:j+1]

                # Case: string[i] != string[j], then DP[i][j] = 0
                else:
                    dp[i][j] = 0

        print("")
        for row in dp:
            print(row)

        return longest_palindromic_substring
    

    # Note: What does the "i+1 > j-1" do? (In the 'Case: If string[i] == string[j] and DP[i+1][j-1] = 1, 
    # then DP[i][j] = 1')
    # ChatGPT explanation:
    # """
    # Great — you're asking the perfect question!
    # Let's go very carefully, because this is very deep and important for understanding substring DP problems:

    # 📖 What does this mean:
    # i+1 > j-1 or dp[i+1][j-1] == 1

    # 🧠 Let's break it:
    # You are trying to decide whether the substring s[i..j] is a palindrome.

    # Two things must happen:
    # 1. s[i] == s[j]
    # 2. The inside substring s[i+1..j-1] must also be a palindrome
    # ✅ That’s how normal palindromes work — first letter and last letter match, and the inside is also a 
    # palindrome.

    # BUT!!
    # If the inside substring is empty or invalid,
    # then you don’t need to check it — because an empty substring is trivially a palindrome!

    # That's why:
    # 📌 When i+1 > j-1 happens:
    # - i+1 means the character after i
    # - j-1 means the character before j

    # If:
    #       i+1>j−1
    # then the "inside substring" s[i+1..j-1] is empty or invalid (no characters between i and j).
    # ✅ An empty inside substring is considered a palindrome by definition.

    # ✨ Simple Examples
    # Example 1: substring "aa"
    # - i = 0
    # - j = 1
    # - i+1 = 1
    # - j-1 = 0
    # - i+1 > j-1 → (1 > 0)
    # Thus, the inside substring s[1..0] is empty
    # ✅ So "aa" is a palindrome if s[i] == s[j].

    # Example 2: substring "aba"
    # - i = 0
    # - j = 2
    # - i+1 = 1
    # - j-1 = 1
    # - i+1 = j-1 → (1 == 1)
    # Inside substring is just "b", a single character, which is trivially a palindrome. 
    # ✅ So you still accept if dp[i+1][j-1] == 1.

    # 📋 Quick Decision Table:
    # Situation	  |    What happens?
    # i+1 > j-1	  |    Inside is empty → accept immediately ✅
    # i+1 <= j-1  |    Inside is non-trivial → must check dp[i+1][j-1]
    # """
    


solution = Solution()
print(solution.longestPalindrome1("babad"))     # "bab"
print(solution.longestPalindrome1("cbbd"))      # "bb"
print(solution.longestPalindrome1("a"))         # "a"

print(solution.longestPalindrome2("babad"))       # "bab"
print(solution.longestPalindrome2("cbbd"))        # "bb"
print(solution.longestPalindrome2("a"))           # "a"
