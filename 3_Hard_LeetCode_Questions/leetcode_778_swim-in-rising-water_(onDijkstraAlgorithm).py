# With HEAVY reference to this solution: https://www.youtube.com/watch?v=amvrKlMLuGY (Neetcode) (YouTube video by Neetcode titled, 
# 'Swim in Rising Water - Dijkstra's Algorithm - Leetcode 778 - Python') (particularly the idea that the
# algorithm to solve this leetcode question is using Dijkstra's algorithm, and how to structure the node 
# entries to be added into the min heap in the format of '(max(current node, previous node), row, column)')


# Also with reference to the video: https://www.youtube.com/watch?v=71Z-Jpnm3D4 (Carl the Person) (YouTube video by Carl the Person titled, 
# 'Dijkstra's Algorithm Visualized and Explained') (to learn the theory/pseudocode of the Dijkstra's algorithm)


# What is Dijkstra's algorithm?
# Dijkstra's algorithm aims to find the shortest path from one node to all other vertices. It does so by 
# repeatedly selecting the nearest unvisited node and calculating the distance to all the unvisited 
# neighboring vertices (greedy). It only works for edges with positive weights. 

# You can think of Dijkstra's algorithm as basically a version of a greedy Breadth First Search (BFS)
# algorithm, where you search a graph level by level, and then only taking the path that gives you the
# shortest weight/distance (which in code, you can track via a min-heap).

# To handle edges with negative weights, we use the Bellman Ford algorithm, which also aims to find the 
# shortest path from one node to all other vertices, but it is slower as it is not greedy.

# Source: https://www.geeksforgeeks.org/dsa/what-are-the-differences-between-bellman-fords-and-dijkstras-algorithms/ (GeekforGeeks)


# Pseudocode:
# In this question, all we care about is about finding the path with the smallest max elevation.

# 1. Starting from the source node, we do a modified Dijkstra's algorithm, whereby we still initialize
#    a 'visited' hash table/set to track if a node has already been visited, and a min heap
#    (Side note: the 'visited' hash table/set can either be used to:
#     - just track if a node has already been visited (usually just a set will do)
#     - track both, if a node has already been visited, and the shortest distance/weight to each node
#       in the graph (will need a hash table)
#     depending on how you implement the Dijkstra's algorithm
#    )

#   In this case, we do not care about finding the shortest distance/weight to each node
#   in the graph, we only care about the end node, so we will just be using a 'visited' set

# 2. Since in this question, we just need to find the path with the smallest max elevation, we need to
#    somehow keep track of the current max elevation down each path. We can track that by in each
#    entry in the min heap, we put it in this format:
#           (max(current node, previous node), row, column)

# 3. Doing the standard Dijkstra's algorithm
#    - while min heap
#    - pop current node from min heap
#    - if popped current node is already visited/in 'visited' set, continue
#    - else, 
#      => add popped current node into the 'visited' set
#      => for each neighbor coordinates, and checking if it is within bounds and that this neighbor is
#         not yet in 'visited' set, push it into the min heap, in the specified format:
#           (max(current node, previous node), row, column)
#    - if we encounter the end node, we can break out of the loop early, and return the 
#      max(current node, previous node), which will be the max elevation of the path with the smallest 
#      max elevation


import heapq

class Solution:
    def swimInWater(self, grid: list[list[int]]) -> int:
        # up down left right
        directions = [[-1,0], [1,0], [0,-1], [0,1]]
        visited = set()
        min_heap = [(grid[0][0], 0, 0)]

        while min_heap:
            curr = heapq.heappop(min_heap)
            if (curr[1], curr[2]) in visited:
                continue

            if (curr[1], curr[2]) == (len(grid) - 1, len(grid[0]) - 1):
                return curr[0]

            visited.add((curr[1], curr[2]))
            # print(visited)

            for i in range(4):
                if 0 <= curr[1] + directions[i][0] < len(grid) and 0 <= curr[2] + directions[i][1] < len(grid[0]) and (curr[1] + directions[i][0], curr[2] + directions[i][1]) not in visited:
                    heapq.heappush(min_heap, (max(curr[0], grid[curr[1] + directions[i][0]][curr[2] + directions[i][1]]), curr[1] + directions[i][0], curr[2] + directions[i][1]))

        return -1



solution = Solution()
print(solution.swimInWater([[0,2],[1,3]]))      # 3
print(solution.swimInWater([[0,1,2,3,4],[24,23,22,21,5],[12,13,14,15,16],[11,17,18,19,20],[10,9,8,7,6]]))       # 16