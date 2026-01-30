# How to convert a decimal to binary?
# E.g. For the decimal 18,

# 1. Dividing by 2 throughout the rows
#    Current number   |  Quotient
#          18        / 2      0
#           9        / 2      1
#           4        / 2      0
#           2        / 2      0
#           1        / 2      1

# 2. Put the quotient into a string you get: 01001
# 3. Reverse the string to get the binary of the decimal 18 = 10010


# How to add 2 binaries such that you get a resulting binary corresponding to the decimal that 
# is the result of the addition of the decimals?
# E.g. For the addition of 2 (binary of 10) and 3 (binary of 11)

# Step 1: Write numbers aligned by place value
#   1 0  ← 2 in binary (1×2 + 0×1)
# + 1 1  ← 3 in binary (1×2 + 1×1)
# --------


# Step 2: Start from rightmost column (ones/2⁰ place)
# Column 1: 0 + 1 = 1
#   1 0
# + 1 1
# --------
#       1  ← Write 1 in ones place, no carry

# Step 3: Move to next column (twos/2¹ place)
# Column 2: 1 + 1 = 10 in binary
# - This is 2 in decimal, which is "10" in binary
# - We MUST regroup: Write 0, carry 1 to next column
# 1
#   1 0
# + 1 1
# --------
#     0 1  ← Write 0 in twos place

# Step 4: Handle the carry
# Since we carried 1 from column 2, and there are no more columns left:
# - Create a new column (fours/2² place)
# - Write the carried 1
# 1
#   1 0
# + 1 1
# --------
#   1 0 1  ← Final answer: 101₂

# Therefore, by adding (10) (decimal of 2) with (11) (decimal of 3), we get (101) (decimal of 5) 
# as the final answer.


# Sources:
# - https://www.wikihow.com/Add-Binary-Numbers (Wikihow) (for how to convert decimal to binary)
# - https://www.cuemath.com/numbers/binary-addition/ (cuemath) (for how to add 2 binaries such
#   that you get a resulting binary corresponding to the decimal that is the result of 
#   the addition of the decimals)


# ///////////////////////////////////////////////////////////////////////////////////


# Approach 1: My approach (fails, as it does not handle negative numbers, only positive numbers)
# class Solution:
#     def getSum(self, a, b):
#         # Get binary form of the 2 integers
#         not_yet_a_binary = ''
#         not_yet_b_binary = ''

#         while a >= 1:
#             # Add the quotients of each division by 2 into the string
#             not_yet_a_binary += str(a % 2)
#             a = a // 2

#         while b >= 1:
#             # Add the quotients of each division by 2 into the string
#             not_yet_b_binary += str(b % 2)
#             b = b // 2

#         a_binary = list(reversed(not_yet_a_binary))
#         b_binary = list(reversed(not_yet_b_binary))
#         print(a_binary)
#         print(b_binary)


#         # Add the 2 binaries together using the bitwise AND operator, '&', and XOR operator, '^'
#         # Figuring out which binary is longer
#         longer_binary = ''
#         shorter_binary = ''
#         if len(a_binary) > len(b_binary):
#             longer_binary = a_binary 
#             shorter_binary = b_binary 
#         elif len(a_binary) < len(b_binary):
#             longer_binary = b_binary 
#             shorter_binary = a_binary 
#         else:
#             longer_binary = a_binary 
#             shorter_binary = b_binary 

#         # Fill longer binary with an additional 0 at the front, and fill shorter binary with
#         # additional 0s at the front such that its length matches the longer binary
#         longer_binary = ['0'] + (longer_binary)
#         additional_zeroes = ['0'] * (len(longer_binary) - len(shorter_binary))
#         shorter_binary = additional_zeroes + shorter_binary

#         print(longer_binary)
#         print(shorter_binary)

#         carry_required = False
#         result_binary = ''
#         i = 0
#         while i < len(longer_binary):
#             print(len(longer_binary)-i-1)
#             # Check if need consider carry forward
#             if carry_required:
#                 if int(longer_binary[len(longer_binary)-i-1]) == 1 and int(shorter_binary[len(longer_binary)-i-1]) == 1:
#                     result_binary = '1' + result_binary
#                 elif (int(longer_binary[len(longer_binary)-i-1]) == 0 and int(shorter_binary[len(longer_binary)-i-1]) == 1) or (int(longer_binary[len(longer_binary)-i-1]) == 1 and int(shorter_binary[len(longer_binary)-i-1]) == 0):
#                     result_binary = '0' + result_binary
#                 else:
#                     result_binary = '1' + result_binary
#                     carry_required = False
            
#             else:
#                 result_binary = str(int(longer_binary[len(longer_binary)-i-1]) ^ int(shorter_binary[len(longer_binary)-i-1])) + result_binary
#                 if int(longer_binary[len(longer_binary)-i-1]) == 1 and int(shorter_binary[len(longer_binary)-i-1]) == 1:
#                     carry_required = True
#                 else:
#                     carry_required = False
                
            
#             i += 1
#             print(result_binary)


#         # Convert the result binary back into decimal
#         result = 0
#         for i in range(len(result_binary) - 1, - 1, -1):
#             print(f"i, {i}")
#             print(f"result_binary[i], {result_binary[i]}")
#             result += int(int(result_binary[len(result_binary)-i-1]) * pow(2,i))

#         return result


# ///////////////////////////////////////////////////////////////////////////////////


# With HEAVY reference to these solutions: 
# - https://www.youtube.com/watch?v=gVUrDV4tZfY (Neetcode) (YouTube video by Neetcode titled, 'Sum of Two Integers - Leetcode 371 - Java')
# - https://leetcode.com/problems/sum-of-two-integers/solutions/489210/read-this-if-you-want-to-learn-about-mas-jf8d/?envType=problem-list-v2&envId=oq45f3x3
#   (Leetcode) (Leetcode solution by INRA)

# Approach 2: Neetcode's approach (works)
# Pseudocode:
# 1. Apply bitwise XOR operation, '^' to the binaries of the 2 numbers, to get a new binary
# 2. Apply bitwise AND operation, '&' to the binaries of the 2 numbers
# 3. Apply bitwise left-shift, '<<' to the result of the bitwise AND operation, '&' to the binaries 
#    of the 2 numbers, to get another new binary, which represents the 'carry forward' binary
# 4. Repeat step 1 to 3, using the 2 new binaries until the result of Step 2 and 3 becomes 0, which
#    means there is no more 'carry forward' binary and you are done

# Important note: Python's bitwise operations, '^', '&' and '<<' all work on decimals! No need to convert decimal to binary and vice
#                 versa seperately like I did in Approach 1, simply passing the decimal to the bitwise operations in Python is fine.
class Solution:
    def getSum(self, a, b):

        # You also need to do masking! (from INRA's solution)
        # What is masking?
        # A bitmask is a value you do the bitwise AND operator, '&'', with another number to keep only the bits you care about and 
        # clear the rest.
        mask = 0xffffffff       # 32 bit mask in hexadecimal

        while (b & mask) != 0:
            new_binary_1 = a ^ b
            b = a & b
            new_binary_2 = b << 1

            a = new_binary_1
            b = new_binary_2

            # print(a)
            # print(b)

        return (a & mask) if b > 0 else a
    

solution = Solution()
print(solution.getSum(1,2))     # 3
print(solution.getSum(2,3))     # 5
print(solution.getSum(100,2))   # 102
print(solution.getSum(20,30))   # 50
print(solution.getSum(-1,1))    # 0