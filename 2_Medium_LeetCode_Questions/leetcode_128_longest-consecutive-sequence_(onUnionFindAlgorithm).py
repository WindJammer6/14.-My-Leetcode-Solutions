# Using Union Find Algorithm,
# Sources: 
# - https://www.youtube.com/watch?v=ayW5B2W9hfo (Potato Coders) (Youtube video by Potato Coders
#   titled 'Union Find in 5 minutes — Data Structures & Algorithms')
# - https://www.geeksforgeeks.org/introduction-to-disjoint-set-data-structure-or-union-find-algorithm/
#   (GeekforGeeks)

# The Union Find Algorithm has 2 important operations/functions,
# 1. Find:
# The task is to find representative of the set of a given element. The representative is always root 
# of the tree. So we implement find() by recursively traversing the parent array until we hit a node 
# that is root (parent of itself).

# 2. Union: 
# The task is to combine two sets and make one. It takes two elements as input and finds the 
# representatives of their sets using the Find operation, and finally puts either one of the trees 
# (representing the set) under the root node of the other tree.


# Using the code implementation of Union Find Algorithm from GeekforGeeks
class UnionFindAlgorithm:
    def __init__(self, list):
      
        # Initialize the parent array with each 
        # element as its own representative
        self.parent = {}
        for i in list:
            self.parent[i] = i 
    
    # This is the 'find()' function without path compression optimisation. 
    def find_without_path_compression_optimisation(self, i):
      
        # If i itself is root or representative
        if self.parent[i] == i:
            return i

        # print(f"parent[i] {self.parent[i]}")
        # print(f"i {i}")

        # Else recursively find the representative 
        # of the parent
        return self.find(self.parent[i])
    

    # This is the 'find()' function with path compression optimisation. You can read about this
    # in the GeekforGeeks page on the Union Find Algorithm.
    def find(self, i):      
        if self.parent[i] != i:
            self.parent[i] = self.find(self.parent[i])
        return self.parent[i]
        
    
    def union(self, i, j):
      
        # Representative of set containing i
        irep = self.find(i)
        
        # Representative of set containing j
        jrep = self.find(j)
        
        # Make the representative of i's set
        # be the representative of j's set
        self.parent[irep] = jrep


class Solution:
    def longestConsecutive(self, nums):
        if nums == []:
            return 0
        
        # Use set instead of lists for a faster lookup time of O(1)! Lists have a lookup time of O(n).
        # This is also used to remove duplicate elements in the array, as sets remove duplicate elements 
        # automatically and only stores all unique elements
        nums_set = set(nums)
        union_find_algorithm = UnionFindAlgorithm(nums_set)

        for num in nums_set:
            if num + 1 in nums_set:
                union_find_algorithm.union(num, num + 1)

        # print(union_find_algorithm.parent)
        # print(index)



        # Get the corresponding representatives for all the elements in the parent dictionary
        # Whichever representative that appears the most, the count of it appearing is the length 
        # of the longest subsequence
        
        # Method 1: The 'count()' function is very costly, causing time exceeded error! (not optimised)
        # all_values_in_dictionary = list(union_find_algorithm.parent.values())
        # # print(all_values_in_dictionary)
        # representative_with_largest_group = max(union_find_algorithm.parent, key=all_values_in_dictionary.count)
        # return all_values_in_dictionary.count(representative_with_largest_group)

        # Method 2: Count sizes of connected components (sets) (more optimised)
        group_sizes = {}
        for num in nums_set:
            rep = union_find_algorithm.find(num)
            if rep not in group_sizes:
                group_sizes[rep] = 0
            group_sizes[rep] += 1

        # Return the size of the largest group
        return max(group_sizes.values())

        

solution = Solution()
nums1 = [100,4,200,1,3,2]
nums2 = [0,3,7,2,5,8,4,6,0,1]
nums3 = [1,0,1,2]
print(solution.longestConsecutive(nums1))       # 4
print(solution.longestConsecutive(nums2))       # 9
print(solution.longestConsecutive(nums3))       # 3