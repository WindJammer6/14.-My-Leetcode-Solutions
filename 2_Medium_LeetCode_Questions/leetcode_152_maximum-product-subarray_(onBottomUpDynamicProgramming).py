# With HEAVY reference to this solution: https://www.youtube.com/watch?v=lXVy6YWFcRM&t=2s (Neetcode) (YouTube video by Neetcode titled, 'Maximum Product Subarray - Dynamic Programming - Leetcode 152')

# For every number, save the current max and current min value seen so far. 

# Why save current min? 
# Because it is to consider negative values. If the next number is a negative number, multiplying
# the min (which is likely a negative value) with the next negative number, might give you the 
# max positive number for the next number. (see the video solution link above for a better
# explanation)

# (IMPORTANT NOTE: The current min is not the minimum possible value we've seen so far, it is 
#                  the minimum possible value for all subarrays which includes the current number)

# Using an example:
# nums = [2,3,-2,4,0,3]

# Let:
# index       0     1      2      3      4     5
# nums        2     3     -2      4      0     3
# max/min    2/2   6/3   6/-12  24/-48  1/1   3/1   (note that for index 1 it is '6/3',
#                                                     not '6/2'!)  
# global max  4     6      6      24     24    24   (tracks the largest max product
#     (we instantiate                                 we've seen so far)
#   the 'global max' with 
#       'max(nums)')
            
# How do we handle zeros?
# Since 0 kinda kills the streak, as it causes both the current max and current min to both become
# 0, and even future current max and current min to also stay at 0, we instead 'reset' the
# current max and min to both become 1 instead. We let both become 1 instead because it is like
# a neutral value, and as we continue to the next number, our streak can continue again.


# Why do we need a 'global max', and why do we instantiate it as 'max(nums)'?
# This is purely to handle the edge cases where 0 is the max product.

# Using another example for these edge cases,
# nums = [-2,0,-1]

# Let:
# index       0     1      2
# nums       -2     0     -1
# max/min   -2/-2  1/1   -1/-1

# global max  0     0      0
#     (we instantiate
#   the global max with 
#       'max(nums)')



# Recurrence:
# max_ending_at_current_index[i] = max(nums[i], 
#                                  nums[i] * max_ending_at_current_index[i-1], 
#                                  nums[i] * min_ending_at_current_index[i-1])
                     
# min_ending_at_current_index[i] = min(nums[i],
#                                  nums[i] * max_ending_at_current_index[i-1],
#                                  nums[i] * min_ending_at_current_index[i-1])

# Subproblems:
# For each position i in the array, compute:
# - dp1[i] ~ max_ending_here[i]: The maximum product subarray that MUST END at position i
# - dp2[i] ~ min_ending_here[i]: The minimum product subarray that MUST END at position i

# Base cases:
# - if nums[0] is not 0,
#   -> at nums[0], dp1[0] = nums[0] and dp2[0] = nums[0] 
# - else (nums[0] is 0),
#   -> at nums[0], dp1[0] = 1 and dp2[0] = 1 


class Solution:
    def maxProduct(self, nums):
        dp1 = []                    # stores all the current max
        dp2 = []                    # stores all the current min
        global_max = max(nums)

        if nums[0] != 0:            # Base case
            dp1.append(nums[0])
            dp2.append(nums[0])
        else:
            dp1.append(1)
            dp2.append(1)

        for i in range(1, len(nums)):
            # print(f"Current value: {nums[i]}")
            if nums[i] != 0:
                current_max = max(nums[i], dp1[-1] * nums[i], dp2[-1] * nums[i])
                current_min = min(nums[i], dp1[-1] * nums[i], dp2[-1] * nums[i])
                dp1.append(current_max)
                dp2.append(current_min)

                # Check if need update the 'global_max'
                # (Note: No need to check if 'nums[i]' will ever be the max value as it won't be
                #        since that case is already handled when the 'global_max' is instantiated
                #        as 'max(nums)')
                if current_max > global_max:
                    global_max = current_max

            else:
                dp1.append(1)
                dp2.append(1)

            # print(dp1)
            # print(dp2)
            # print(global_max)

        return global_max
    

solution = Solution()
print(solution.maxProduct([2,3,-2,4]))      # 6
print(solution.maxProduct([-2,0,-1]))       # 0
print(solution.maxProduct([2,3,-2,4,0,3]))  # 6
print(solution.maxProduct([-4,-3]))         # 12
print(solution.maxProduct([2,-5,-2,-4,3]))  # 24