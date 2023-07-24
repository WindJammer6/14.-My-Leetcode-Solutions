class Solution:
    def runningSum(self, nums: list[int]) -> list[int]:
        duplicate_nums_list = []

        for i in nums:
            duplicate_nums_list.append(i)
        print(duplicate_nums_list)


        temp_list = []

        index_in_nums_list = 0
        index_in_duplicate_nums_list = 0

        while index_in_nums_list < len(nums):

            temp_number = 0

            if index_in_duplicate_nums_list != index_in_nums_list:
                while index_in_nums_list != index_in_duplicate_nums_list:
                    temp_number += duplicate_nums_list[index_in_duplicate_nums_list]
                    index_in_duplicate_nums_list += 1
                    print(index_in_duplicate_nums_list)

            temp_number += duplicate_nums_list[index_in_duplicate_nums_list]

            temp_list.append(temp_number)

            index_in_nums_list += 1
            index_in_duplicate_nums_list = 0
            print(index_in_nums_list)
            print(temp_list)

        return temp_list
            
                
number_list = [3,1,2,10,1]

solution = Solution()

print(solution.runningSum(number_list))