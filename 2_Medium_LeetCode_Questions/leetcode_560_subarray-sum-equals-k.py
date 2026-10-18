# With HEAVY reference to this solution: https://www.youtube.com/watch?v=fFVZt-6sgyo (Neetcode) (YouTube video by Neetcode titled, 
# 'Subarray Sum Equals K - Prefix Sums - Leetcode 560 - Python')


# What is prefix sum?
# Prefix sum is a running total of the array from the start up to each index.


# Pseudocode (it is not intuitive at all and I still don't understand why it works...):
# 1. Setup a hash map as such:
#    Prefix_sum : count (i.e. number of times this prefix sum occured)
#    key        : values

# 2. Initialize the hash map with 1 pair of values {0: 1}, which indicates that a prefix sum of 0 has 
#    occurred once so far — representing the empty subarray before index 0

# 3. Calculate the prefix sum for the array, i.e. for [3,2,-1,5],
#    - First sum (up to index 0) = 3
#    - Second sum (up to index 1) = 3 + 2 = 5
#    - Third sum (up to index 2) = 3 + 2 + -1 = 4
#    - Fourth sum (up to index 3) = 3 + 2 + -1 + 5 = 9

# 4. For each sum, calculate that sum - k. 
#    - if the prefix sum/result of sum - k exists as a key in the hash map, then add its count to the total
#      number of subarrays whose sum equals to k

# 5. For each sum, if that sum already exist as a key in the hash map, increment count by 1, or add its 
#    sum as a key into the hash map with a value of 1

# 6. Return the total number of subarrays whose sum equals to k


class Solution:
    def subarraySum(self, nums, k):
        dictionary = {0 : 1}
        output = 0
        current_sum = 0

        # Doing prefix sum
        for i in range(len(nums)):
            current_sum += nums[i]
            result = current_sum - k
            if result in dictionary:
                output += dictionary[result]
            
            if current_sum in dictionary:
                dictionary[current_sum] += 1
            else:
                dictionary.update({current_sum : 1})

        return output



solution = Solution()
print(solution.subarraySum([1,1,1], 2))     # 2
print(solution.subarraySum([1,2,3], 3))     # 2