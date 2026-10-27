# Important note about implementing max-heap using the heapq Python library:
# The heapq Python library only natively supports min-heap, but there is a way to cheat this, which is by 
# flipping the values using negative to make it behave like a max-heap.

# Example:
#   max_heap = []
#   numbers = [10, 20, 5]

#   # Invert values to simulate a max-heap
#   for num in numbers:
#       heapq.heappush(max_heap, -num)

#   # Retrieve the largest number
#   largest = -heapq.heappop(max_heap)  # Returns 20


import heapq

class Solution:
    def lastStoneWeight(self, stones: list[int]) -> int:
        max_heap = []

        # Create max_heap
        for i in stones:
            max_heap.append(-i)
        heapq.heapify(max_heap)

        while len(max_heap) > 1:
            first_stone = -heapq.heappop(max_heap)
            second_stone = -heapq.heappop(max_heap)
            # print(first_stone)
            # print(second_stone)
            # print(max_heap)

            if first_stone == second_stone:
                pass
            else:
                result_stone = first_stone - second_stone
                heapq.heappush(max_heap, -result_stone)
        
        if len(max_heap) == 1:
            return -max_heap[0]
        else:
            return 0


solution = Solution()
print(solution.lastStoneWeight([2,7,4,1,8,1]))        # 1
print(solution.lastStoneWeight([1]))                  # 1