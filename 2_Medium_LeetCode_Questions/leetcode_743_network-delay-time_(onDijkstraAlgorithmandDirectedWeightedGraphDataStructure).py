# With HEAVY reference to this solution: https://www.youtube.com/watch?v=EaphyqKU4PQ (Neetcode) (YouTube video by Neetcode titled, 
# 'Network Delay Time - Dijkstra's algorithm - Leetcode 743') (particularly the idea that the
# algorithm to solve this leetcode question is using Dijkstra's algorithm, and how he implemented
# Dijkstra's algorithm using a min-heap)


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
# Using Dijkstra's algorithm, since what this algorithm does is that it finds the shortest path 
# distances from the source node to all other vertices in the graph, so the minimum time for the
# signal to reach all nodes is basically the shortest path distance from source node to the 
# furthest node in the graph

# 1. Create the directed weighted graph data structure
# 2. Do Dijkstra's algorithm, and following Neetcode's method of implementing Dijkstra's algorithm using
#    a min-heap:
#    - We first append the source node, with a weight of zero to itself in the format into a min-heap:
#           [weight, node]
#    - Instantiate a 'visited' hash table, this will store the shortest distance from the source node
#      to each node in the graph, as well as to track if a node has already been visited

#    - While the min-heap is not empty:
#      => pop the min-heap. If popped element is in 'visited', continue
#      => add the popped element into the 'visited' hash table to mark the current node as visited
#      => take all of its neighbours 
#      => if the neighbour already exist in the 'visited' hash table, don't push it into the min-heap
#      => else if the neighbour does not exist in the 'visited' hash table, push it into the min-heap,
#         with the total weight, where:
#           total weight = weight_from_source_node_to_current_node + weight_from_parent_node_to_neighbour_node

# 3. To detect if there are unreachable nodes, we check if the length of the 'visited' hash table
#    is equal to n. 
#    - if not equal, this means it is impossible for all n nodes to receive the signal 
#      and return -1
#    = else if equal, based on the 'visited' hash table, return its largest value



import heapq

class Solution:
    def networkDelayTime(self, times: list[list[int]], n: int, k: int) -> int:
        # Create the directed weighted graph data structure as an adjacency list
        graph = {}
        for i in range(len(times)):
            if times[i][0] not in graph:
                graph.update({times[i][0] : [(times[i][2], times[i][1])]}) 
            else:
                graph[times[i][0]].append((times[i][2], times[i][1]))

        # print(graph)


        # Dijkstra's algorithm using a min-heap
        min_heap = [(0, k)]
        visited = {}

        while min_heap:
            popped_element = heapq.heappop(min_heap)
            if popped_element[1] in visited:
                continue
            # print(popped_element)
            
            visited.update({popped_element[1] : popped_element[0]})
            if popped_element[1] in graph:
                for neighbour in graph[popped_element[1]]:
                    if neighbour[1] not in visited:
                        heapq.heappush(min_heap, (popped_element[0] + neighbour[0], neighbour[1]))

        # print(visited)

        if n != len(visited):       # check for unreachable nodes
            return -1
        else:
            output = 0
            for key, value in visited.items():
                if value > output:
                    output = value
            return output



solution = Solution()
print(solution.networkDelayTime([[2,1,1],[2,3,1],[3,4,1]], 4, 2))    # 2
print(solution.networkDelayTime([[1,2,1]], 2, 1))                    # 1
print(solution.networkDelayTime([[1,2,1]], 2, 2))                    # -1