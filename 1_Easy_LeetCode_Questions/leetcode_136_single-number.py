class Solution:
    def singleNumber(self, nums: list[int]) -> int:
        dictionary = {}

        for i in nums:
            if i not in dictionary:
                dictionary.update({i : 1})
            else:
                dictionary[i] += 1

        for key, value in dictionary.items():
            if value != 2:
                return key

nums_list = [4,1,2,1,2]

solution = Solution()

print(solution.singleNumber(nums_list))