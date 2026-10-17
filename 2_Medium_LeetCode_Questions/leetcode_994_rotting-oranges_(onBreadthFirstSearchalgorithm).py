# With some reference to this solution: https://www.youtube.com/watch?v=y704fEOx0s0 (Neetcode) (YouTube 
# video by Neetcode titled, 'Rotting Oranges - Leetcode 994 - Python'), particularly on the part of multi 
# BFS algorithm


# Pseudocode:
# 1. Calculate number of fresh oranges, and look for coordinates of the rotten oranges
# 2. For each rotten orange, start a Breadth First Search (BFS) algorithm starting from it
# 3. For each time step (minutes), take 1 step for each BFS algorithm for each BFS algorithm.
#    For every fresh oranges converted to rotten orange, decrement number of fresh oranges by 1,
#    and change the grid cell from 1 to 2. (see code on how to do this multi BFS algorithm)
# 4. If number of remaining fresh oranges is 0, return number of time step (minutes), else return -1


from collections import deque
# To use deque as a queue, you can:
# - do the O(1) 'append()' function for enqueuing
# - do the O(1) 'popleft()' function for dequeing

# DO NOT USE PYTHON LIST AS A QUEUE! Because while the 'append()' function for enqueuing is O(1),
# the 'pop(0)' function for dequeing is O(n)! Very slow and inefficient! Hence, when doing queue,
# you MUST use the collections library for deque!

class Solution:
    def orangesRotting(self, grid: list[list[int]]) -> int:
        # Find number of fresh oranges and where the rotten oranges are
        fresh_oranges = 0
        queue = deque()        # to store to locations of the rotten oranges

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    fresh_oranges += 1
                elif grid[i][j] == 2:
                    queue.append((i,j))
                else:       # empty cell, where grid[i][j] == 0, don't need to do anything
                    pass

        # Do multi bfs algorithm (one bfs algorithm for each rotten orange)
        directions = [[-1,0], [1,0], [0,-1], [0,1]]
        time = 0

        while queue and fresh_oranges > 0:
            queue_length = len(queue)
            for i in range(queue_length):
                x, y = queue.popleft()
                for i in range(4):
                    if 0 <= x+directions[i][0] < len(grid) and 0 <= y+directions[i][1] < len(grid[0]):
                        if grid[x+directions[i][0]][y+directions[i][1]] == 1:
                            neighbour = (x+directions[i][0], y+directions[i][1])
                            grid[neighbour[0]][neighbour[1]] = 2
                            queue.append(neighbour)
                            fresh_oranges -= 1

            time += 1

        # If number of remaining fresh oranges is 0, return number of time step (minutes), else return -1
        if fresh_oranges != 0:
            return -1
        else: 
            return time


solution = Solution()
print(solution.orangesRotting([[2,1,1],[1,1,0],[0,1,1]]))   # 4
print(solution.orangesRotting([[2,1,1],[0,1,1],[1,0,1]]))   # -1
print(solution.orangesRotting([[0,2]]))   # 0
