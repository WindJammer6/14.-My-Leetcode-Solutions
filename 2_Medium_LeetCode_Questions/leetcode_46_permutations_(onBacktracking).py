# Using backtracking, with inspiration to the '17. Letter Combinations of a Phone Number' leetcode 
# question (their codes are very similar as both uses backtracking)

class Solution:
    def permute(self, nums: list[int]) -> list[list[int]]:
        output = []

        self.backtracking([], nums, nums.copy(), output)

        return output

    def backtracking(self, current_permutation, nums, nums_original, output):
        # Base case occurs when length of 'current_permutation' is equal to length of 'nums_original'
        if len(current_permutation) == len(nums_original):
            output.append(current_permutation)
            return

        # Recursive case
        for i in range(len(nums)):
            self.backtracking(current_permutation + [nums[i]], nums[:i] + nums[i+1:len(nums)], nums_original, output)


solution = Solution()
print(solution.permute([1,2,3]))        # [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]
print(solution.permute([0,1]))          # [[0,1],[1,0]]
print(solution.permute([1]))            # [[1]]