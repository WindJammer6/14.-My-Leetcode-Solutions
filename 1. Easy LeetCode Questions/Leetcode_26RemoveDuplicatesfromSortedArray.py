class Solution:
    def removeDuplicates(self, nums: list[int]) -> int:

        reversed_nums = reversed(nums)

        temp_dictionary = {}
        for index, value in enumerate(reversed_nums):
            temp_dictionary.update({index:value})
        print(temp_dictionary)

        temp_list = []
        non_duplicate_list = []
    
        for index, value in temp_dictionary.items():
            if index - 1 > -1:
                if value != temp_dictionary[index-1]:
                    temp_list.insert(0, value)
                    non_duplicate_list.append(value)
                    print(temp_list)
                else:
                    temp_list.append("_")
                    print(temp_list)

            if index - 1 == -1:
                temp_list.append(value)
                non_duplicate_list.append(value)
            else:
                pass

        nums.clear()
        print(nums)

        for i in temp_list:
            nums.append(i)

        return len(non_duplicate_list)
    
solution = Solution()

nums = [0,0,1,1,1,2,2,3,3,4] # Input list
expectedNums = [0, 1, 2, 3, 4] # The expected answer with correct length

k = solution.removeDuplicates(nums) # Calls your implementation
print(k)
print(nums)
assert k == len(expectedNums)
for i in range(k):
    assert nums[i] == expectedNums[i]