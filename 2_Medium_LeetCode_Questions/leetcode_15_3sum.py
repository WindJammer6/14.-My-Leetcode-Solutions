# Pesudocode:
# 1. Iterate through the list. This is the iterating index.
# 2. For the remaining part of the list (iterating index to end
#    of the list, do the two pointers approach such that 
#    "nums[first_pointer] + nums[second_pointer] + nums[iterating_index] == 0")
# 3. To avoid picking duplicates triplets, you need to:
#    - shift the iterating index to the next position whenever the current number 
#       its at is the same as the previous number it was at 
#    - shift the left or right index to the next position whenever the current number 
#       its at is the same as the previous number it was at 

class Solution:
    def threeSum(self, nums):
        
        nums.sort()

        result = []

        for i in range(0, len(nums)-2):
            firstelement = i
            firstpointer = i + 1
            secondpointer = len(nums) - 1 

            # Checking if current number at iterating index is same as the previous number iterating index 
            # to avoid picking duplicate triplets
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            
            while firstpointer < secondpointer:
                if nums[firstelement] + nums[firstpointer] + nums[secondpointer] < 0:
                    firstpointer += 1
                    # Checking if current number at left pointer is same as the previous number 
                    # left pointer to avoid picking duplicate triplets
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
