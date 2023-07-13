class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        result = []
        for i in range(0, len(nums)):
            for j in range(1, len(nums)-i):
                if nums[i] + nums[i+j] == target:
                    result = [i, i+j]
        return result
    
solution = Solution()
number_list = [2,7,11,15]

print(solution.twoSum(number_list, 9))
    
