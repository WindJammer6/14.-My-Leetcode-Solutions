class Solution:
    def findSubarrays(self, nums):
        memory = {}

        for i in range(len(nums)-1):
            memory.update({i : nums[i] + nums[i+1]})

        memory_values = memory.values()
        memory_values_set = set(memory_values)

        # print(memory_values)
        # print(memory_values_set)

        if len(memory_values_set) < len(nums) - 1:
            return True
        else:
            return False
        

solution = Solution()
print(solution.findSubarrays([4,2,4]))      # true
print(solution.findSubarrays([1,2,3,4,5]))  # false
print(solution.findSubarrays([0,0,0]))      # true