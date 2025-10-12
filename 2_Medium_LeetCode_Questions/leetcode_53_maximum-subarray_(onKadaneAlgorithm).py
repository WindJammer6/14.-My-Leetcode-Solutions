# What is Kadane's algorithm?
# Kadane's Algorithm is a dynamic programming approach used to solve the maximum
# subarray sum problem (this problem). (Even though it is a dynamic programming
# approach it feels more like a greedy approach)

# How Kadane's algorithm works?
# To calculate the maximum sum of subarray ending at current element, say maxEnding,
# we can use the maximum sum ending at the previous element.

# So for any element, we have two choices:
# Choice 1: Extend the maximum sum subarray ending at the previous element by adding 
# the current element to it. If the maximum subarray sum ending at the previous index 
# is positive, then it is always better to extend the subarray.

# Choice 2: Start a new subarray starting from the current element. If the maximum 
# subarray sum ending at the previous index is negative, it is always better to start 
# a new subarray from the current element.

# (Alternatively, you can think of it as at each current element, you can choose 
# either the maximum subarray from the previous index + current element OR just the
# current element only (i.e. start a new subarray from the current element), whichever is larger)

# For the first element, you only have 1 choice which is to simply just add it as part 
# of the subarray.

# Source(s): 
# - https://www.youtube.com/watch?v=86CQq3pKSUw (CS Dojo) (YouTube video by CS Dojo titled, 'Kadane's Algorithm to Maximum Sum Subarray Problem')
# - https://www.geeksforgeeks.org/dsa/largest-sum-contiguous-subarray/ (GeekforGeeks)

class Solution:
    def maxSubArray(self, nums):
        
        # Using Kadane's algorithm
        max_global_subarray_sum = [nums[0]]
        max_global_subarray_sum = nums[0]
        
        max_current_subarray = [nums[0]]
        max_current_subarray_sum = nums[0]

        for i in range(1, len(nums)):
            # If the current element only is larger than the maximum subarray from the previous index + current element
            if nums[i] > max_current_subarray_sum + nums[i]:
                # Choose the current element only (i.e. start a new subarray from the current element)
                max_current_subarray = [nums[i]]
                max_current_subarray_sum = nums[i]
            
            else:
                # Choose the maximum subarray from the previous index + current element
                max_current_subarray.append(nums[i])
                max_current_subarray_sum += nums[i] 

            # print(max_current_subarray)
            # print(max_current_subarray_sum)


            # Checking if maximum subarray up to the current element is larger than the
            # global maximum subarray
            if max_current_subarray_sum > max_global_subarray_sum:
                max_global_subarray_sum = max_current_subarray_sum
                max_global_subarray = max_current_subarray

            # print(max_global_subarray)
            # print(max_global_subarray_sum)
            
        return max_global_subarray_sum             

    
solution = Solution()
print(solution.maxSubArray([-2,1,-3,4,-1,2,1,-5,4]))    # 6
print(solution.maxSubArray([1]))                        # 1
print(solution.maxSubArray([5,4,-1,7,8]))               # 23