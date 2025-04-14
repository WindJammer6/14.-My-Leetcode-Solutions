# The bottom-up dynamic programming (with memoization) code is partially taken from my school's 
# lecture notes, but I identified the recurrence that relates the sub-problems, the sub-problems 
# and base cases for this question and modified the top-down dynamic programming (with memoization) 
# code to this context to answer this question

# Analyzing for potential patterns for the question with trial and error: 
#   Number              Binary              Number of 1s 
#     0                     0                     0
#     1                     1                     1 

#     2                    10                     1 
#     3                    11                     2 

#     4                   100                     1 
#     5                   101                     2 
#     6                   110                     2 
#     7                   111                     3 

#     8                  1000                     1 
#     9                  1001                     2 
#    10                  1010                     2 
#    11                  1011                     3 

#    12                  1100                     2 
#    13                  1101                     3 
#    14                  1110                     3 
#    15                  1111                     4 

#    16                 10000                     1 
#    17                 10001                     2 
#    18                 10010                     2 
#    19                 10011                     3 

#    20                 10100                     2 
#    21                 10101                     3 
#    22                 10110                     3 
#    23                 10111                     4 

#    24                 11000                     2 
#    25                 11001                     3 
#    26                 11010                     3 
#    27                 11011                     4 

#    28                 11100                     3 
#    29                 11101                     4 
#    30                 11110                     4 
#    31                 11111                     5 

#    32                100000                     1
#    33                100001                     2
#    34                100010                     2
#    35                100011                     3

#    36                100100                     2
#    37                100101                     3
#    38                100110                     3
#    39                100111                     4

#    40                101000                     2
#    41                101001                     3
#    42                101010                     3
#    43                101011                     4

#    44                101100                     3
#    45                101101                     4
#    46                101110                     4
#    47                101111                     5

#    48                110000                     2
#    49                110001                     3
#    50                110010                     3
#    51                110011                     4

#    52                110100                     3
#    53                110101                     4
#    54                110110                     4
#    55                110111                     5

#    56                111000                     3
#    57                111001                     4
#    58                111010                     4
#    59                111011                     5

#    60                111100                     4
#    61                111101                     5
#    62                111110                     5
#    63                111111                     6

#    64               1000000                     3


# Observations:
# Numbers with binary of length 1: 0-1 (total: 2 numbers)
# Numbers with binary of length 2: 2-3 (total: 2 numbers)
# Numbers with binary of length 3: 4-7 (total: 4 numbers) = 2 + 2 = 4 = 2^2
# Numbers with binary of length 4: 8-15 (total: 8 numbers) = 2 + 2 + 4 = 8 = 2^3
# Numbers with binary of length 5: 16-31 (total: 16 numbers) = 2 + 2 + 4 + 8 = 16 = 2^4
# ...

# The number of 'Numbers with binary of a particular length' is the sum of all
# number of 'Numbers with binary of all its previous lengths of that particular length'


# dp[0] = 0;
# dp[1] = dp[1-1] + 1;
# dp[2] = dp[2-2] + 1;
# dp[3] = dp[3-2] +1;
# dp[4] = dp[4-4] + 1;
# dp[5] = dp[5-4] + 1;
# dp[6] = dp[6-4] + 1;
# dp[7] = dp[7-4] + 1;
# dp[8] = dp[8-8] + 1;
# dp[9] = dp[9-8] + 1;
# dp[10] = dp[10-8] + 1;
# dp[11] = dp[11-8] + 1;
# dp[12] = dp[12-8] + 1;
# dp[13] = dp[13-8] + 1;
# dp[14] = dp[14-8] + 1;
# dp[15] = dp[15-8] + 1;
# ..


# Sub-problems to solve:
# "What is the value of the next element in the array based on the previous elements?"


# Recurrence:
# Let DP(k) be the next element in the array
#       DP(k) = DP(i−offset) + 1
# where offset is the largest power of 2 ≤ i, which acts as the base for a new group.


# Base cases:
# - When i = 0, ans[i] = 0
#   oR DP(0) = 0

# - When i = 1, ans[i] = 1
#   OR DP(1) = 1


# Pseudocode:
# Using bottom-up dynamic programming (with tabulation): 

#  function count_bits(n): 
#  Require: n is a non-negative integer
#  1. array dp ← empty list  
#  2. for i from 0 to n, do
#  3.     if i == 0 then
#  4.         append 0 to dp
#  5.     else
#  6.         offset ← 1
#  7.         while offset * 2 ≤ i, do
#  8.             offset ← offset * 2
#  9.         value ← dp[i - offset] + 1
# 10.         append value to dp

# 11. return dp


class Solution:
    def countBits(self, n: int) -> list[int]:
        dp = []  # bottom-up tabulation array

        for i in range(n + 1):
            if i == 0:              # Base case 1
                dp.append(0)        # tabulation code
            else:
                offset = 1
                while offset * 2 <= i:
                    offset *= 2
                dp.append(dp[i - offset] + 1)   # Recurrence that relates the sub-problems

        return dp
            

solution = Solution()
print(solution.countBits(2))   # [0,1, 1]
print(solution.countBits(5))   # [0,1, 1,2, 1,2]
print(solution.countBits(10))  # [0,1, 1,2, 1,2,2,3, 1,2,2]
print(solution.countBits(20))  # [0,1, 1,2, 1,2,2,3, 1,2,2,3,2,3,3,4, 1,2,2,3,2,3]