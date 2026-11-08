# With HEAVY reference to this solution: https://www.youtube.com/watch?v=dJ7sWiOoK7g (Neetcode) (YouTube video by Neetcode titled, 
# 'Jump Game II - Greedy - Leetcode 45 - Python')


# Pseudocode:
# Using a greedy approach. There is a dynamic programming approach to this, but Neetcode recommends
# the greedy approach as it is faster, with time complexity of O(n), while the dynamic programming approach
# has a time complexity of O(n^2)
# 1. We do a sort of Breadth First Search (BFS) algorithm, where you search in levels, where each level
#    represents the minimum number of jumps it will take to reach a particular index. You start with the 
#    first index as the 0th level (as it takes no jumps to reach this index)
# 2. Using the value at the 0th index, we find out which subsequent values it can reach based on the
#    value at the 0th index. These indexes will become the 1st level (as it takes no jumps to reach these
#    indexes) (if the value at the 0th index is 2, then it can reach the 1st and 2nd index, which will be
#    part of the 1st level)
# 3. Using the value in each index in the 1st level, we find which subsequent indexes it can reach, which 
#    will form the 2nd level. We can mark the range of subsequent indexes it can reach with a left and 
#    right pointer in code.
# 4. We keep doing this until we find out what level the end index n-1 falls under, as it represents
#    the minumum number of jumps it will `take to reach a particular index.

# For example:
#   [2,3,1,1,4]
#    0 1 1 2 2  level



class Solution:
    def jump(self, nums: list[int]) -> int:
        level = 0
        # To mark the range of indexes that falls in the current level
        left_pointer = 0
        right_pointer = 0

        while right_pointer < len(nums)-1:
            new_right_pointer = right_pointer
            for i in range(left_pointer, right_pointer+1):
                if i + nums[i] > right_pointer and i + nums[i] > new_right_pointer:
                    new_right_pointer = i + nums[i]
                
            left_pointer = right_pointer + 1
            right_pointer = new_right_pointer
            level += 1

        return level


solution = Solution()
print(solution.jump([2,3,1,1,4]))       # 2
print(solution.jump([2,3,0,1,4]))       # 2
print(solution.jump([0]))               # 0
print(solution.jump([2,1,1,1,1]))       # 3