# With HEAVY reference to this solution: https://www.youtube.com/watch?v=HAgLH58IgJQ (Neetcode) (YouTube 
# video by Neetcode titled, 'Reverse Integer - Bit Manipulation - Leetcode 7 - Python')


# From the perspective of Python, why does this problem look too easy?
# From ChatGPT:
# Integer overflow occurs when a calculation produces a value that exceeds the maximum or minimum range an 
# integer data type can represent. For example, a signed 32-bit integer has a range of -2^{31} to 2^{31}-1 
# (−2,147,483,648 to 2,147,483,647). Adding 1 to the maximum value causes integer overflow. In languages 
# like Java, this causes the integer to wrap around to the minimum value, whereas in C and C++, signed 
# integer overflow results in undefined behavior.

# Python generally does not suffer from integer overflow because its built-in int type supports arbitrary 
# precision, meaning it dynamically allocates additional memory to accommodate larger integers, unlike 
# fixed-width integer types in languages such as Java and C++. However, this comes at the cost of 
# potentially higher memory consumption and slower arithmetic operations. 


# Pseudocode:
# The mathematical solution for this is as such, which works for all programming languages
# 1. To extract out a digit from a number, i.e. lets say 3 from 123, we can do modulo % by 10, as it
#    will give you 3 as the remainder. And to move on to the next digit, i.e. lets say 2 in 123, we can do
#    division by 10 rounded down, as it will give you 12. You can then repeat this process to 'iterate'
#    through the number
# 2. Max number is 2^31 - 1 = 2147483647 and min number is -2^31 = -2147483648. The trick to this is to 
#    - firstly, check if the current number, is larger than the max number or smaller than the min number 
#      without its last digit (and you can find this by doing max_number // 10 or min_number // 10). If it 
#      is, that means this value is going to overflow and we return 0, otherwise, we can return the 
#      reversed number without overflow
#    - secondly, check if the current number is equal to the max number or smaller than the min number 
#      without its last digit, further check if that next digit is larger than than last digit of the max 
#      number or smaller than the last digit of the min number. If it is, that means this value is going 
#      to overflow and we return 0, otherwise, we can return the reversed number without overflow

import math 

class Solution:
    def reverse(self, x: int) -> int:
        max_number = 2147483647 
        min_number = -2147483648

        result = 0
        while x != 0:
            current_digit = int(math.fmod(x, 10))
            x = int(x / 10)

            if (result > max_number // 10) or (result == max_number // 10 and current_digit > 7):
                return 0
            elif (result < int(min_number / 10) or (result == int(min_number / 10) and current_digit < -8)):
                return 0
            else:
                result = (result * 10) + current_digit

        return result 



solution = Solution()
print(solution.reverse(123))      # 321
print(solution.reverse(-123))     # -321
print(solution.reverse(120))      # 21