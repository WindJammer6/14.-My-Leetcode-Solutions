#Big O Notation of O(n^2) solution via brute force approach:
class Solution:
    def twoSumbruteforce(self, nums: list[int], target: int) -> list[int]:
        result = []
        for i in range(0, len(nums)):
            for j in range(1, len(nums)-i):
                if nums[i] + nums[i+j] == target:
                    result = [i, i+j]
        return result
    
#Big O Notation of O(n) solution via two pointers approach:
    def twoSumtwopointers(self, nums: list[int], target: int) -> list[int]:

        #List needs to be sorted for the two pointers approach to work
        nums_copy = nums.copy()
        nums_copy.sort()

        frontpointer = 0
        backpointer = len(nums) - 1

        while frontpointer < backpointer:
            if nums_copy[frontpointer] + nums_copy[backpointer] < target:
                frontpointer += 1

            if nums_copy[frontpointer] + nums_copy[backpointer] > target:
                backpointer -= 1

            if nums_copy[frontpointer] + nums_copy[backpointer] == target:
                print(nums_copy[frontpointer], nums_copy[backpointer])

                #For the case if both numbers are the same (e.g. 3 + 3 = 6 (target))
                if nums_copy[frontpointer] == nums_copy[backpointer]:

                    print(nums[nums.index(nums_copy[frontpointer]) + 1 : ])
                    reduced_nums_list = nums[nums.index(nums_copy[frontpointer]) + 1 : ]
                    for i in reduced_nums_list:
                        if i == nums_copy[frontpointer]:
                            return [nums.index(nums_copy[frontpointer]), reduced_nums_list.index(i) + nums.index(nums_copy[frontpointer]) + 1]

                #For the case if both numbers are different (e.g. 2 + 4 = 6 (target))   
                return [nums.index(nums_copy[frontpointer]), nums.index(nums_copy[backpointer])]
            
        return -1
    
    
solution = Solution()

number_list = [3,3]

print(solution.twoSumbruteforce(number_list, 6))

print(solution.twoSumtwopointers(number_list, 6))
    
