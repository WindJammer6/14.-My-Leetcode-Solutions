class Solution:
    def findMin(self, nums):
        # Using binary search algorithm to find the change in sequence flux due to the rotations
        n = len(nums)

        if 0 < n < 3:
            smallest = 10000
            for i in nums:
                if i < smallest:
                    smallest = i
            return smallest

        left_index = 0
        right_index = n - 1
        middle_index = (right_index + left_index) // 2

        while (right_index >= left_index):
            print(f"R {right_index}")
            print(f"L {left_index}")
            print(f"M {middle_index}")
            if nums[middle_index - 1] > nums[middle_index]:
                return nums[middle_index]

            elif nums[middle_index + 1] < nums[middle_index]:
                return nums[middle_index + 1]

            if nums[right_index] < nums[middle_index]:
                left_index = middle_index
                middle_index = (right_index + left_index) // 2

            elif nums[left_index] > nums[middle_index]:
                right_index = middle_index
                middle_index = (right_index + left_index) // 2

            elif (nums[left_index] < nums[middle_index]) and (nums[right_index] > nums[middle_index]):
                break

        return nums[0]
    
solution = Solution()
print(solution.findMin([3,4,5,1,2]))        # 1
print(solution.findMin([4,5,6,7,0,1,2]))    # 0
print(solution.findMin([11,13,15,17]))      # 11