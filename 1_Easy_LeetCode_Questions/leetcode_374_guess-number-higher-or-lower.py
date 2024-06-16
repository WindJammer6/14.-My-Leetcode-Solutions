# The guess API is already defined for you.
# @param num, your guess
# @return -1 if num is higher than the picked number
#          1 if num is lower than the picked number
#          otherwise return 0
# def guess(num: int) -> int:

# How the 'guess()' self-made function might look like:
# (where 'num' represents the number guessed by the player)
def guess(num):
    pick = 2
    if num > pick:
        return -1
    elif num < pick:
        return 1
    else:
        return 0



# This brute force method fails because its Big O Notation of Time Complexity is O(n), causing the
# error 'Time exceeded'.
# class Solution:
#     def guessNumber(self, n: int) -> int:

#         guessed_number = 10

#         while True:
#             higher_equal_lower = guess(guessed_number)
            
#             # This means that the 'guessed_number' is higher than the picked number
#             if higher_equal_lower == 1:
#                 guessed_number += 1
#             # This means that the 'guessed_number' is lower than the picked number
#             elif higher_equal_lower == -1:
#                 guessed_number -= 1
#             # This means that the 'guessed_number' is equal than the picked number
#             else:
#                 return guessed_number
#             print(guessed_number)



# Using more efficient Search Algorithms with better Big O Notation of Time Complexity to find the 
# number being picked.

# Using the Iterative Binary Search Algorithm, which has a Big O Notation of Time Complexity of 
# O(log n)
class Solution:
    def guessNumber(self, n: int) -> int:

        # The Iterative Binary Search Algorithm
        left_limit = 0
        right_limit = n
        
        while left_limit <= right_limit:
            guessed_number = (left_limit + right_limit) // 2
            higher_equal_lower = guess(guessed_number)

            if higher_equal_lower == 0:
                return guessed_number
            
            if higher_equal_lower == 1:
                left_limit = guessed_number + 1
            else:
                right_limit = guessed_number - 1

            print(f"'guessed_number': {guessed_number}")
            
        # If the picked number is not in specified range of numbers that the picked number can be 
        # chosen from, here we will 'return -1'
        return -1


range_of_numbers_that_the_picked_number_can_be_chosen_from = 2

solution = Solution()

print(solution.guessNumber(range_of_numbers_that_the_picked_number_can_be_chosen_from))