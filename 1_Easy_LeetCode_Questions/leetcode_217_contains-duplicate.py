class Solution:
    def containsDuplicate(self, nums: list[int]) -> bool:
        temp_dictionary = {}

        for i in nums:
            if i in temp_dictionary:
                temp_dictionary[i] += 1
            else:
                temp_dictionary.update({i:1})

        for index, value in temp_dictionary.items():
            if value > 1:
                return True
            
        return False

number_list = [1,2,3,1]

solution = Solution()

print(solution.containsDuplicate(number_list))