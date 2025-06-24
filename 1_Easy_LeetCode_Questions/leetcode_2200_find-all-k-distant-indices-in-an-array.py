import heapq

class Solution:
    def findKDistantIndices(self, nums, key, k):
        # Putting all the elements from nums into a Priority Queue/Heap Queue
        pq = []
        k_distant_indices = []
        equal_key = []

        # Finding all j for nums[j] == key
        for j in range(len(nums)):
            heapq.heappush(pq, j)
            if nums[j] == key:
                equal_key.append(j)

        index_equal_key = 0
        while pq:
            smallest_element = heapq.heappop(pq)
            # print(f"{smallest_element} and {equal_key[index_equal_key]}")

            if abs(smallest_element - equal_key[index_equal_key]) <= k:
                k_distant_indices.append(smallest_element)

            if (smallest_element - equal_key[index_equal_key] >= k) and (index_equal_key < len(equal_key)-1):
                index_equal_key += 1

        return k_distant_indices
    

solution = Solution()
print(solution.findKDistantIndices([3,4,9,1,3,9,5], 9, 1))      # [1,2,3,4,5,6]
print(solution.findKDistantIndices([2,2,2,2,2], 2, 2))          # [0,1,2,3,4]