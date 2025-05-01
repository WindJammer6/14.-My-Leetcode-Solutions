class Solution:
    def switchTwoElementsPositionsInPlace(self, nums, i, j):
        temp = nums[i]
        nums[i] = nums[j]
        nums[j] = temp

    def moveZeroes(self, nums):
        """
        Do not return anything, modify nums in-place instead.
        """
        for i in range(len(nums)-1, -1, -1):
            
            if nums[i] == 0:
                for j in range(i, len(nums)):
                    if nums[j] == 0:
                        print(nums)
                        if j+1 < len(nums):
                            self.switchTwoElementsPositionsInPlace(nums, j, j+1)
                    else:
                        break
                        
        return nums
    

solution = Solution()
print(solution.moveZeroes([0,1,0,3,12]))        # [0]
print(solution.moveZeroes([0]))                 # [1,3,12,0,0]