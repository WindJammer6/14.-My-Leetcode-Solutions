# With HEAVY reference to this solution: https://www.youtube.com/watch?v=ZI2z5pq0TqA (Neetcode) (YouTube video by Neetcode titled, 
# 'Trapping Rain Water - Google Interview Question - Leetcode 42')


# Pseudocode:
# 1. The pattern is basically at every index, the number of rain water it can fill is:
#       min(max(left_of_index), max(right_of_index)) - height[index] (i.e. height/value at that index)

# 2. The only other optimisation here is to optimise the space complexity of the solution from O(n) to O(1)
#    on how to track the maximum of the left of index and maximum of the right of index
#    - The space complexity of O(n) for this is to store them in a 2D array, of the maximum of the left of 
#      index and maximum of the right of index
#    - The space complexity of O(1) for this is to use the two pointers approach, where you:
#      => Initialize two pointers at the start and end of the array,
#         and two variables (left_max and right_max), with left_max set to height at index 0,
#         and right_max set to height at index len(height)-1.
#      => While the left pointer < right pointer:
#         -> Compare left_max and right_max to determine which
#            pointer to process:
#            - If left_max < right_max:
#                Calculate trapped water at the left pointer:
#                max(0, left_max - height[left_pointer])
#                Add it to the total.
#                Move the left pointer one position right.
#                Update the left_max if height[left_pointer] > left_max.
#            - Otherwise:
#                Calculate trapped water at the right pointer:
#                max(0, right_max - height[right_pointer])
#                Add it to the total.
#                Move the right pointer one position left.
#                Update the right_max if height[right_pointer] > right_max 
#      => Repeat until the two pointers cross.


class Solution:
    def trap(self, height: list[int]) -> int:
        left_pointer = 0
        right_pointer = len(height) - 1
        maximum_left_of_index = height[0]
        maximum_right_of_index = height[len(height) - 1]

        output = 0
        current_index = left_pointer

        while left_pointer < right_pointer:
            if maximum_left_of_index < maximum_right_of_index:
                if maximum_left_of_index - height[current_index] > 0:
                    output += maximum_left_of_index - height[current_index]
                left_pointer += 1
                current_index = left_pointer
                if height[left_pointer] > maximum_left_of_index:
                    maximum_left_of_index = height[left_pointer]
            else:
                if maximum_right_of_index - height[current_index] > 0:
                    output += maximum_right_of_index - height[current_index]
                right_pointer -= 1
                current_index = right_pointer
                if height[right_pointer] > maximum_right_of_index:
                    maximum_right_of_index = height[right_pointer]

        return output


solution = Solution()
print(solution.trap([0,1,0,2,1,0,1,3,2,1,2,1]))        # 6
print(solution.trap([4,2,0,3,2,5]))                    # 9