# Approach 1: Brute Force approach
# But this approach is quite bad in terms of time complexity 

# Pseudocode:
# 1. the '__init__' function will initially sort the provided nums
# 2. the 'add' function will:
#    - append the element into nums
#    - sort nums again in descending order
#    - retrieve the kth largest element
# (alternatively you can do a slight optimization of doing binary search algorithm to find the place to add
# the new element in the sorted list so you don't need to do sorting again, but this is still quite poor
# in terms of time and space complexity)


# class KthLargest:

#     def __init__(self, k: int, nums: list[int]):
#         self.k = k
#         nums.sort()
#         self.nums = nums

#     def add(self, val: int) -> int:
#         self.nums.append(val)
#         self.nums.sort()
#         # print(self.nums)
#         return self.nums[len(self.nums) - self.k]
        

# //////////////////////////////////////////////////////////////////


# With some reference to this solution: https://www.youtube.com/watch?v=hOjcdrqMoQ8 (Neetcode) (YouTube video by Neetcode titled, 
# 'Kth Largest Element in a Stream - Leetcode 703 - Python') (particularly on the idea of using min-heap of size k)

# Approach 2: Using min-heap of size k

# Pseudocode:
# 1. Based on the initial nums, take the top k elements and form a min-heap using them. Note that it is
#    not computationally efficient in terms of time complexity to sort the initial nums, and then add
#    the top k elements, so you shouldn't do this! One more efficient way to do this is just convert
#    the whole initial nums to a min-heap, and then keep popping the root nodes until the size
#    of the min-heap becomes k
# 2. As new elements get added,
#    - if it is smaller or equal to the root node of the min-heap, don't need to do anything to the 
#      min-heap
#    - else if it is larger than the root node of the min-heap, add this new element into the min-heap,
#      and pop the root node from the min-heap. The new root node of the min-heap will now be the kth
#      largest element and return this its value


import heapq

class KthLargest:

    def __init__(self, k: int, nums: list[int]):
        self.k = k
        self.nums = nums
        self.min_heap_of_size_k = nums.copy()
        heapq.heapify(self.min_heap_of_size_k)
        while len(self.min_heap_of_size_k) > k:
            heapq.heappop(self.min_heap_of_size_k)
        # print(self.min_heap_of_size_k)

    def add(self, val: int) -> int:
        self.nums.append(val)

        if len(self.min_heap_of_size_k) < self.k:
            heapq.heappush(self.min_heap_of_size_k, val)
            return self.min_heap_of_size_k[0]

        else:           # 'len(self.min_heap_of_size_k) == k', as the min-heap of size k will never have a 
                        # size larger than k
            if self.min_heap_of_size_k and val <= self.min_heap_of_size_k[0]:
                return self.min_heap_of_size_k[0]
            else:
                heapq.heappush(self.min_heap_of_size_k, val)
                popped_element = heapq.heappop(self.min_heap_of_size_k)
                return self.min_heap_of_size_k[0]



# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)

obj = KthLargest(3, [4, 5, 8, 2])
print(obj.add(3)) 
print(obj.add(5)) 
print(obj.add(10))
print(obj.add(9)) 
print(obj.add(4)) 

# Input:
# ["KthLargest","add","add","add","add","add"]
# [[3,[4,5,8,2]],[3],[5],[10],[9],[4]]
# Expected Output:
# [null,4,5,5,8,8]


obj = KthLargest(4, [7, 7, 7, 7, 8, 3])
print(obj.add(2)) 
print(obj.add(10))
print(obj.add(9)) 
print(obj.add(9)) 

# Input:
# ["KthLargest","add","add","add","add"]
# [[4,[7,7,7,7,8,3]],[2],[10],[9],[9]]
# Expected Output:
# [null,7,7,7,8]


obj = KthLargest(1, [])
print(obj.add(-3))
print(obj.add(-2))
print(obj.add(-4))
print(obj.add(0)) 
print(obj.add(4)) 

# Input:
# ["KthLargest","add","add","add","add","add"]
# [[1,[]],[-3],[-2],[-4],[0],[4]]
# Expected Output:
# [null,-3,-2,-2,0,4]