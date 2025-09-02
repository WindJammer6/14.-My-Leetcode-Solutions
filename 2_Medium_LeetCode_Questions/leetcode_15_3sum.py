class Solution:
    def threeSum(self, nums):
        
        nums.sort()

        result = []

        for i in range(0, len(nums)-2):
            firstelement = i
            firstpointer = i + 1
            secondpointer = len(nums) - 1 

            if i > 0 and nums[i] == nums[i - 1]:
                continue
            
            while firstpointer < secondpointer:
                if nums[firstelement] + nums[firstpointer] + nums[secondpointer] < 0:
                    firstpointer += 1
                    while (firstpointer < secondpointer) and (nums[firstpointer] == nums[firstpointer - 1]):
                        firstpointer += 1
                    # print(firstpointer)
                elif (firstpointer < secondpointer) and (nums[firstelement] + nums[firstpointer] + nums[secondpointer] > 0):
                    secondpointer -= 1
                    while (firstpointer < secondpointer) and (nums[secondpointer] == nums[secondpointer + 1]):
                        secondpointer -= 1
                    # print(secondpointer)
                else:       # nums[firstelement] + nums[firstpointer] + nums[secondpointer] == 0
                    result.append([nums[firstelement], nums[firstpointer], nums[secondpointer]])

                    firstpointer += 1
                    secondpointer -= 1
                    while (firstpointer < secondpointer) and (nums[firstpointer] == nums[firstpointer - 1]):
                        firstpointer += 1
                    while (firstpointer < secondpointer) and (nums[secondpointer] == nums[secondpointer + 1]):
                        secondpointer -= 1

        print(result)

        return result


solution = Solution()
print(solution.threeSum([-1,0,1,2,-1,-4]))  # [[-1,-1,2],[-1,0,1]]
print(solution.threeSum([0,1,1]))  # []
print(solution.threeSum([0, 0, 0]))  # [[0, 0, 0]]