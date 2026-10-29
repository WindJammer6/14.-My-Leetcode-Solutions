# This leetcode question literally just asks you to implement the Binary Search Algorithm

class Solution:
    def search(self, nums: list[int], target: int) -> int:
        left = 0
        right = len(nums) - 1

        while left <= right:
            mid = (left + right) // 2
            if nums[mid] == target:
                return mid
            
            elif target > nums[mid]:
                left = mid + 1
            else:       # target < nums[mid]
                right = mid - 1

        return -1



solution = Solution()
print(solution.search([-1,0,3,5,9,12], 9))     # 4
print(solution.search([-1,0,3,5,9,12], 2))     # 1