# With HEAVY reference to this solution: https://www.youtube.com/watch?v=1vZswirL8Y8 (Neetcode) (YouTube video by Neetcode titled, 
# 'Multiply Strings - Leetcode 43 - Python')


# Purpose of this leetcode question (by ChatGPT): 
# The problem isn't about banning the * operator — it's about the fixed bit-width limit of standard 
# integer types. In most languages, int/long max out at 32/64 bits (roughly 10–19 decimal digits), but the 
# inputs here can be up to 200 digits. So even if you convert the strings to integers, they'd overflow and 
# give wrong results. The challenge is to implement big-number multiplication manually (typically 
# grade-school digit-by-digit with carry handling) so it works for arbitrarily large numbers. The * you 
# saw in solutions is usually Python's string repetition ('0' * n for padding/zero-shifting), not integer 
# multiplication — and using it that way is perfectly allowed.


# Pseudocode:
# 1. Here is how you do multiplication of larger numbers without using a calculator manually
#    - Taking the example of 15 x 16, you multiply each of the top numbers (5 and 2) with the first 
#      bottom number (6), then you do it again for the second bottom number (5), etc.
#    - You might potentially have a carry forward (e.g. when you do 5 x 6 = 30, the carry forward is 3)
#        15
#      x 56
#      ----
#        30     doing 5 x 6

#        15
#      x 56
#      ----
#        30     doing 1 x 6
#        6
#      ----
#        90

#        15
#      x 56
#      ----
#        90     doing 5 x 5
#       25
#      ----
#       340

#        15
#      x 56
#      ----
#       340     doing 1 x 5
#       5
#      ----
#       840

# 2. We first pre-allocate the memory needed for the product of the 2 strings. We can tell that the
#    number of digits/memory needed is at most the sum of the length of both number strings (e.g.
#    99 x 99 = 9801, product is 2 digits + 2 digits = 4 digits long)

# 3. To implement step 1 in code, we do individual mulplication of 2 digits (which will give us at most a 
#    2 digit number), and we can obtain:
#    - the ones place by doing modulo (%) of 10 to get the remainder (e.g. 81 % 10 = 1)
#    - the tens place by doing division (//) of 10 as it will round down (e.g. 81 // 10 = 8)

# 4. The position in the output array where the product of any of the two digits should be added is 
#    determined by the sum of their indices, assuming both numbers are indexed from right to left 
#    (in reverse, starting at 0).

# 5. Throughout the code, we handle the indexing of both strings and result in reverse


class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        # Pre-define the length of the list for the product of the 2 strings
        output = []
        for i in range(len(num1) + len(num2)):
            output.append(0)
        # print(output)

        # Reverse the 2 strings
        num1 = num1[::-1]
        num2 = num2[::-1]

        for i in range(len(num1)):
            for j in range(len(num2)):
                result = int(num1[i]) * int(num2[j]) + output[i+j]

                # Get ones place
                ones_place = result % 10
                output[i+j] = ones_place

                # Get tens place
                tens_place = result // 10
                output[i+j+1] += tens_place


        # Need to get rid of any leading zeroes
        output = output[::-1]           # correct the reversed output/product by reversing it
        output_string = ""
        
        beginning = 0
        while beginning < len(output) and output[beginning] == 0:
            beginning += 1

        for i in range(beginning, len(output)):
            output_string += str(output[i])

        if output_string:
            return output_string
        # To factor in cases where the product is 0, which will cause 'output_string' to become an empty
        # string ("")
        else:
            return "0"



solution = Solution()
print(solution.multiply("2", "3"))                  # "6"
print(solution.multiply("123", "456"))              # "56088"
print(solution.multiply("99", "99"))                # "9801"
print(solution.multiply("9133", "0"))               # "0"
print(solution.multiply("123456789", "987654321"))  # "121932631112635269"