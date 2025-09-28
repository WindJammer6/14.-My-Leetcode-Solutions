class Solution:
    def search(self, nums, target):
        # Using binary search algorithm to find the change in sequence flux due to the rotations
        n = len(nums)

        if 0 < n < 3:
            for i in range(n):
                if nums[i] == target:
                    return i
            return -1

        left_index = 0
        right_index = n - 1
        middle_index = (right_index + left_index) // 2
        
        while (right_index - 1 > left_index):
            # print(f"R {right_index}")
            # print(f"L {left_index}")
            # print(f"M {middle_index}")
            # print(f"nM {nums[middle_index]}")
            # print(f"T {target}")

            # Split the arrays into 3 subarrays:
            # - Middle
            # - Left subarray
            # - Right subarray

            if nums[middle_index] == target:
                return middle_index

            if nums[left_index] == target:
                return left_index

            if nums[right_index] == target:
                return right_index

            # If left subarray is sorted, hence right subarray is not sorted
            if nums[left_index] < nums[middle_index]:
                # If target is in the sorted left subarray
                if (nums[left_index] <= target <= nums[middle_index]):
                    right_index = middle_index - 1
                    middle_index = (right_index + left_index) // 2
                # If target is not in the sorted left subarray
                else:
                    left_index = middle_index + 1
                    middle_index = (right_index + left_index) // 2                

            # Else left subarray is not sorted, hence right subarray is sorted
            else:
                # If target is in the sorted right subarray
                if (nums[middle_index] <= target <= nums[right_index]):
                    left_index = middle_index + 1
                    middle_index = (right_index + left_index) // 2
                # If target is not in the sorted right subarray
                else:
                    right_index = middle_index - 1
                    middle_index = (right_index + left_index) // 2  

            if nums[middle_index] == target:
                return middle_index

            if nums[left_index] == target:
                return left_index

            if nums[right_index] == target:
                return right_index


        return -1


solution = Solution()
print(solution.search([4,5,6,7,0,1,2], 0))      # 4
print(solution.search([4,5,6,7,0,1,2], 3))      # -1
print(solution.search([1], 0))                  # -1