class Solution:
    def removeElement(self, nums: list[int], val: int) -> int:

        temp_dictionary = {}
        for index, value in enumerate(nums):
            temp_dictionary.update({index:value})
        print(temp_dictionary)

        for index, value in temp_dictionary.items():
            if value == val:
                temp_dictionary[index] = "_"
        
        print(temp_dictionary)

        nums.clear()
        print(nums)

        for index, value in temp_dictionary.items():
            if value == "_":
                nums.append(value)
            else:
                nums.insert(0, value)

        print(nums)

        number_of_elements_that_is_not_val = 0
        for i in nums:
            if i != "_":
                number_of_elements_that_is_not_val += 1

        return number_of_elements_that_is_not_val
    
solution = Solution()

number_list = [0,1,2,2,3,0,4,2] # Input array
val = 2  # Value to remove
expectedNums = [0,0,1,3,4]  # The expected answer with correct length.
                                        # It is sorted with no values equaling val.

k = solution.removeElement(number_list, val)
print(k)

assert k == len(expectedNums)
number_list[:k] = sorted(number_list[:k])
print(number_list)

for i in range(len(expectedNums)):
    assert number_list[i] == expectedNums[i]

print(solution.removeElement(number_list, 3))