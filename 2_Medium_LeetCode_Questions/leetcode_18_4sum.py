# Pesudocode:
# 1. Iterate through the list. This is the iterating index 1.
# 2. Start another iteration through the list. This is the iterating index 2.
# 3. For the remaining part of the list (iterating index 2 to end
#    of the list, do the two pointers approach such that 
#    "nums[first_pointer] + nums[second_pointer] + nums[iterating_index_1] + nums[iterating_index_2]
#    == target")
# 4. To avoid picking duplicates triplets, you need to:
#    - shift the iterating index 1 to the next position whenever the current number 
#       its at is the same as the previous number it was at 
#    - shift the iterating index 2 to the next position whenever the current number 
#       its at is the same as the previous number it was at 
#    - shift the left or right index to the next position whenever the current number 
#       its at is the same as the previous number it was at 

class Solution:
    def fourSum(self, nums: list[int], target: int) -> list[list[int]]:
        output = []
        nums.sort()
        # print(nums)

        for i in range(len(nums)):
            # Checking if current number at iterating index 1 is same as the previous number iterating index 
            # to avoid picking duplicate triplets
            if i > 0 and nums[i] == nums[i-1]:
                continue

            for j in range(i+1, len(nums)):
                # Checking if current number at iterating index 2 is same as the previous number iterating index 
                # to avoid picking duplicate triplets
                if j > i+1 and nums[j] == nums[j-1]:
                    continue

                left = j + 1
                right = len(nums) - 1
                while right > left:
                    # print(f"{i},{j},{left},{right}")
                    if nums[i] + nums[j] + nums[left] + nums[right] == target:
                        output.append([nums[i], nums[j], nums[left], nums[right]])
                        left += 1
                        # Checking if current number at left pointer is same as the previous number 
                        # left pointer to avoid picking duplicate triplets
                        while nums[left] == nums[left-1] and right > left:
                            left += 1
                    
                    elif nums[i] + nums[j] + nums[left] + nums[right] < target:
                        left += 1

                    else:
                        right -= 1

        return output


solution = Solution()
print(solution.fourSum([1,0,-1,0,-2,2], 0))  # [[-2,-1,1,2],[-2,0,0,2],[-1,0,0,1]]
print(solution.fourSum([2,2,2,2,2], 8))  # [[2,2,2,2]]