# Approach 1: Brute force method (works, in O(n) time complexity)
class Solution:
    def topKFrequent(self, nums, k):
        dictionary = {}

        for num in nums:
            if num in dictionary:
                dictionary[num] += 1
            else:
                dictionary[num] = 1

        k_most_frequent_elements = []

        for j in range(k):
            # Get first key in the dictionary
            most_frequent_element = next(iter(dictionary))

            for index, (key, value) in enumerate(dictionary.items()):
                if value > dictionary[most_frequent_element]:
                    most_frequent_element = key

            k_most_frequent_elements.append(most_frequent_element)
            dictionary.pop(most_frequent_element)

        k_most_frequent_elements.sort()

        return k_most_frequent_elements


# Approach 2: Using Quick Select Algorithm (works, in O(n) time complexity)

# About the Quick Select Algorithm:
# Quickselect is a selection algorithm to find the k-th smallest element in an unordered list. 
# It is related to the quick sort sorting algorithm.

# The algorithm is similar to Quick Sort Algorithm. The difference is, instead of recurring for 
# both sides (after finding pivot/partitioned element), it recurs only for the part that contains 
# the k-th smallest element. 

# The logic is simple, 
# - If index of the pivot/partitioned element is more than k, then we recur for the left part. 
# - If index of the pivot/partitioned element is less than k, then we recur for the right part. 
# - If index of the pivot/partitioned element is the same as k, we have found the k-th smallest 
#   element and we return. 

#   This reduces the expected time complexity from O(n log n) to O(n), with a worst-case of O(n^2).

# Sources: 
# - https://www.youtube.com/watch?v=BP7GCALO2v8 (Techdose) (Youtube video by Techdose
#   titled 'Quick Select Algorithm | Efficient searching algorithm')
# - https://www.geeksforgeeks.org/quickselect-algorithm/ (GeekforGeeks)

class Solution2:

    # Code of the Quick Sort Algorithm taken from my Quick Sort Algorithm I created in the '15.-Common-Searching-And-Sorting-Algorithm-Implementations-Python'
    # repository that I took from the Youtube video by codebasics titled 'Quick Sort - Data Structures & Algorithms Tutorial Python #15'
    # Source: 
    # - https://www.youtube.com/watch?v=5iSZ7mh_RAk (codebasics) (Youtube video by codebasics titled 'Quick Sort - Data Structures 
    #   & Algorithms Tutorial Python #15')

    # Quick Sort Algorithm:
    # def swapping_two_elements_in_a_list(self, a, b, array):
    #     if array[a] != array[b] and a != b:
    #         temp = array[a]
    #         array[a] = array[b]
    #         array[b] = temp


    # def hoare_partition_scheme(self, number_list, start_index_of_list, end_index_of_list):
    
    #     pivot_index = start_index_of_list
    #     pivot = number_list[pivot_index]

    #     start_pointer = pivot_index + 1
    #     end_pointer = end_index_of_list

    #     while start_pointer <= end_pointer:

    #         while start_pointer < len(number_list) and number_list[start_pointer] <= pivot:
    #             start_pointer += 1

    #         while number_list[end_pointer] > pivot:
    #             end_pointer -= 1

    #         if start_pointer < end_pointer:
    #             self.swapping_two_elements_in_a_list(start_pointer, end_pointer, number_list)  
                
    #     self.swapping_two_elements_in_a_list(pivot_index, end_pointer, number_list)

    #     return end_pointer


    # def lomuto_partition_scheme(self, number_list, start_index_of_list, end_index_of_list):
    
    #     pivot = number_list[end_index_of_list]
    #     partition_index = start_index_of_list

    #     for i in range(start_index_of_list, end_index_of_list):
    #         if number_list[i] <= pivot:
    #             self.swapping_two_elements_in_a_list(i, partition_index, number_list)
    #             partition_index += 1

    #     self.swapping_two_elements_in_a_list(partition_index, end_index_of_list, number_list)

    #     return partition_index


    # def quick_sort(self, number_list, start_index_of_list, end_index_of_list):

    #     if start_index_of_list >= end_index_of_list:
    #         return

    #     else:
    #         #Just change the 'hoare_partition_scheme' function here to 'lomuto_partition_scheme' function to carry out the Quick Sort Algorithm via Lomuto Partition scheme instead
    #         #of via Hoare Partition scheme
    #         partitioning_point = self.hoare_partition_scheme(number_list, start_index_of_list, end_index_of_list)
    #         self.quick_sort(number_list, start_index_of_list, partitioning_point - 1)
    #         self.quick_sort(number_list, partitioning_point + 1, end_index_of_list)


    # /////////////////////////////////////////////////////////////////////////////////////


    # Modified the Quick Sort Algorithm to become the Quick Select Algorithm (the Quick Select
    # Algorithm is itself also modified here to fit the context of this question to answer it)
    def swapping_two_elements_in_a_list(self, a, b, array):
        if array[a] != array[b] and a != b:
            temp = array[a]
            array[a] = array[b]
            array[b] = temp


    def hoare_partition_scheme(self, number_list, start_index_of_list, end_index_of_list):
    
        pivot_index = start_index_of_list
        pivot = number_list[pivot_index]

        start_pointer = pivot_index + 1
        end_pointer = end_index_of_list

        while start_pointer <= end_pointer:
            
            # Original Quick Select Algorithm does not have the '[1]'. The '[1]' is added here to 
            # fit the context of this question to answer it
            # while start_pointer < len(number_list) and number_list[start_pointer] <= pivot:
            while start_pointer < len(number_list) and number_list[start_pointer][1] <= pivot[1]:
                start_pointer += 1

            # Original Quick Select Algorithm does not have the '[1]'. The '[1]' is added here to 
            # fit the context of this question to answer it
            # while number_list[end_pointer] > pivot:
            while number_list[end_pointer][1] > pivot[1]:
                end_pointer -= 1

            if start_pointer < end_pointer:
                self.swapping_two_elements_in_a_list(start_pointer, end_pointer, number_list)  
                
        self.swapping_two_elements_in_a_list(pivot_index, end_pointer, number_list)

        return end_pointer


    def lomuto_partition_scheme(self, number_list, start_index_of_list, end_index_of_list):
    
        pivot = number_list[end_index_of_list]
        partition_index = start_index_of_list

        for i in range(start_index_of_list, end_index_of_list):
            # Original Quick Select Algorithm does not have the '[1]'. The '[1]' is added here to 
            # fit the context of this question to answer it
            # if number_list[i] <= pivot:
            if number_list[i][1] <= pivot[1]:
                self.swapping_two_elements_in_a_list(i, partition_index, number_list)
                partition_index += 1

        self.swapping_two_elements_in_a_list(partition_index, end_index_of_list, number_list)

        return partition_index


    def quick_select(self, number_list, start_index_of_list, end_index_of_list, k):

        if start_index_of_list >= end_index_of_list:
            return number_list[k]

        else:
            #Just change the 'hoare_partition_scheme' function here to 'lomuto_partition_scheme' function to carry out the Quick Select Algorithm via Lomuto Partition scheme instead
            #of via Hoare Partition scheme
            partitioning_point = self.hoare_partition_scheme(number_list, start_index_of_list, end_index_of_list)

            # The logic is simple, 
            # - If index of the pivot/partitioned element is more than k, then we recur for the left part. 
            if partitioning_point > k:
                return self.quick_select(number_list, start_index_of_list, partitioning_point - 1, k)

            # - If index of the pivot/partitioned element is less than k, then we recur for the right part. 
            elif partitioning_point < k:
                return self.quick_select(number_list, partitioning_point + 1, end_index_of_list, k)

            # - If index of the pivot/partitioned element is the same as k, we have found the k-th smallest 
            #   element and we return. 
            else:
                return number_list[k]



    def topKFrequent(self, nums, k):
        dictionary = {}

        for num in nums:
            if num in dictionary:
                dictionary[num] += 1
            else:
                dictionary[num] = 1

        frequency_of_elements = []
        for index, (key, value) in enumerate(dictionary.items()):
            frequency_of_elements.append((key, value))
        
        k_most_frequent_elements = []
        for i in range(len(frequency_of_elements) - k, len(frequency_of_elements)):
            frequency_of_elements_copy = frequency_of_elements[:]
            kth_smallest_element = self.quick_select(frequency_of_elements_copy, 0, len(frequency_of_elements) - 1, i)
            k_most_frequent_elements.append(kth_smallest_element[0])

        return k_most_frequent_elements



solution = Solution()
print(solution.topKFrequent([1,1,1,2,2,3], 2))      # [1,2]
print(solution.topKFrequent([1], 1))                # [1]
print(solution.topKFrequent([3,0,1,0], 1))          # [0]
print(solution.topKFrequent([1,2], 2))              # [1,2]

solution2 = Solution2()
print(solution2.topKFrequent([1,1,1,2,2,3], 2))      # [1,2]
print(solution2.topKFrequent([1], 1))                # [1]
print(solution2.topKFrequent([3,0,1,0], 1))          # [0]
print(solution2.topKFrequent([1,2], 2))              # [1,2]