#For this Leetcode question, I effectively just copied-pasted the Merge Sort Algorithm's code, which is an in-place Sorting Algorithm
#as the answer, which obviously dosen't use Python's 'sort()' function
def merge_two_smaller_sorted_lists_to_a_merged_sorted_list(smaller_sorted_list_a, smaller_sorted_list_b, array):

    i = j = k = 0

    while i < len(smaller_sorted_list_a) and j < len(smaller_sorted_list_b):
        if smaller_sorted_list_a[i] <= smaller_sorted_list_b[j]:
            array[k] = smaller_sorted_list_a[i]
            i += 1

        else:
            array[k] = smaller_sorted_list_b[j]
            j += 1
        k += 1

    while i < len(smaller_sorted_list_a):
        array[k] = smaller_sorted_list_a[i]
        i += 1
        k += 1

    while j < len(smaller_sorted_list_b):
        array[k] = smaller_sorted_list_b[j]
        j += 1
        k += 1


class Solution:
    def sortColors(self, nums: list[int]) -> None:
    # def merge_sort(array):

        if len(nums) <= 1:
            return nums
        
        middle_element_index = len(nums)//2
        
        left_smaller_subarray = nums[:middle_element_index]
        right_smaller_subarray = nums[middle_element_index:]

        self.sortColors(left_smaller_subarray)
        self.sortColors(right_smaller_subarray)

        merge_two_smaller_sorted_lists_to_a_merged_sorted_list(left_smaller_subarray, right_smaller_subarray, nums)


number_list = [2,0,2,1,1,0]

solution = Solution()

solution.sortColors(number_list)

print(number_list)
