# With HEAVY reference to this solution: https://www.youtube.com/watch?v=s8p8ukTyA2I (Neetcode) (YouTube video by Neetcode titled, 
# 'Task Scheduler - Leetcode 621 - Python')


# Pseudocode:
# Rationale - to minimize the number of CPU intervals required to complete all tasks, we need to  
# prioritise tasks that have the largest count, while keeping track of the cooldown time for another same 
# label task to be completed again

# Note: 
# - We actually don't really need to store the name of the tasks i.e. "A", "B", etc. anywhere in the 
#   algorithm
# - To solve this problem we will be using 2 types of data structures, 
#   -> a priority queue/heap (specifically a max-heap) to keep track of tasks with highest count/priority
#   -> a queue to keep track of interval gap for each task


# 1. Store ONLY (no need the name of the tasks) the count of each of the tasks in this format in a 
#    max-heap priority queue. Keep track of time steps starting from 0.
# 2. For each step, pop the element from the max-heap priority queue, and then decrement its count
#    by 1, then push the '(count, time_to_join_back_priority_queue)' into the queue. Note that 
#    time_to_join_back_priority_queue = time_of_task_completion + n_intervals.
# 3. When current time step = time_to_join_back_priority_queue for the front element in the queue,
#    append it into the max-heap priority queue
# 4. If for a task, the count = 0, then no more need to push anything into the queue
# 5. Keep doing steps 2 to 4 until the max-heap priority queue and queue is empty
# 6. Return total time steps


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
from collections import deque

class Solution:
    def leastInterval(self, tasks: list[str], n: int) -> int:
        # Get counts for each tasks
        dictionary = {}
        max_heap_priority_queue = []

        for i in tasks:
            if i not in dictionary:
                dictionary.update({i : 1})
            else:
                dictionary[i] += 1
        
        for key, value in dictionary.items():
            heapq.heappush(max_heap_priority_queue, -value)
        
        # print(max_heap_priority_queue)


        # Task scheduler algorithm
        time = 0
        queue = deque()

        # print(len(max_heap_priority_queue))

        while len(max_heap_priority_queue) != 0 or len(queue) != 0:
            time += 1

            if max_heap_priority_queue:
                task_done_count = -heapq.heappop(max_heap_priority_queue)
                task_done_count -= 1
                if task_done_count != 0:
                    queue.append((task_done_count, time + n))

            if queue:
                if queue[0][1] == time:
                    task_now_available = queue.popleft()
                    heapq.heappush(max_heap_priority_queue, -task_now_available[0])

        return time


solution = Solution()
print(solution.leastInterval(["A","A","A","B","B","B"], 2))     # 8
print(solution.leastInterval(["A","C","A","B","D","B"], 1))     # 6
print(solution.leastInterval(["A","A","A", "B","B","B"], 3))    # 10