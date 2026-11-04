# With HEAVY reference to this solution: https://www.youtube.com/watch?v=5eIK3zUdYmE (Neetcode) (YouTube video by Neetcode titled, 
# 'Bellman-Ford - Cheapest Flights within K Stops - Leetcode 787 - Python') (particularly the idea that the
# algorithm to solve this leetcode question is using Bellman Ford algorithm, and how he implemented
# Bellman Ford algorithm)


# Also with reference to the video: https://www.youtube.com/watch?v=obWXjtg0L64 (Michael Sambol) (YouTube video by Michael Sambol titled, 
# 'Bellman-Ford in 5 minutes — Step by step example') (to learn the theory/pseudocode of the Bellman Ford algorithm)


# What is the Bellman Ford algorithm?
# Similar to the Dijkstra's algorithm, the Bellman Ford algorithm also aims to find the shortest path 
# from one node to all other vertices. It first calculates the shortest distances which have at-most one edge in the path. Then, it calculates the shortest paths with at-most 2 edges, and so on. After the i-th iteration of outer loop, the shortest paths with at most i edges are calculated. There can be maximum |V| – 1 edge in any simple path, that is why the outer loop runs |v| – 1 time. The idea is, assuming that there is no negative weight cycle if we have calculated shortest paths with at most i edges, then an iteration over all edges guarantees to give the shortest path with at-most (i+1) edges.

# It can handle edges with negative weights, unlike Dijkstra's algorithm.

# Source: https://www.geeksforgeeks.org/dsa/what-are-the-differences-between-bellman-fords-and-dijkstras-algorithms/ (GeekforGeeks)


# Why can't we use Dijkstra's algorithm here?
# We could, but it won't be easy and efficient due to the at most k stops limit. It is easier to do it 
# using the Bellman Ford algorithm.


# Pseudocode:
# 1. Create the directed weighted graph data structure
# 2. Using a slightly modified Bellman Ford algorithm (due to the at most k stops limit),
#    - Instantiate a 'shortest' hash table, this will store the shortest weight/distance from the source 
#      node to each node in the graph based on that current iteration. We instantiate it with all the 
#      nodes with a value of infinity, except for the source node (with index 0), which will have a value 
#      of 0.

#    - While the iterations is less than k + 1 iterations (the usual Bellman Ford algorithm
#      needs to you to run less than n iterations):
#      (Side note:
#       - the Bellman Ford algorithm should only run at most n-1 iterations (assuming no negative 
#         cycles), because the longest possible simple path in a graph with n nodes has n-1 edges, to 
#         visit all n distinct nodes in a line you need n-1 connections
#       - Running a full last n-th iteration can be used as a check: if any shortest distance 
#         still improves, a negative cycle exists, but that's not relevant in this leetcode question
#      )
#      => Instantiate a 'temp' hash table as well, which will be copy of the 'shortest' hash table 
#         (unique to this slightly modified Bellman Ford algorithm, not required for the usual Bellman 
#         Ford algorithm) (see Neetcode's solution for the rationale for this 'temp' hash table)
#      => for each current node (starting from the source node (with index 0)), if the shortest weight 
#         for the current node is infinity, we have yet to know the path to reach this node from the 
#         source node, continue (skip this current node)
#      => for each of the current node's neighbour, calculate the total weight to that neighbour by:
#               total weight = shortest weight of current node in 'shortest' hash table + weight to that 
#                              neighbour from current node
#      => if this total weight is less than the current shortest weight for that neighbour in 'temp'
#         hash table, update the shortest weight to this new total weight in the 'temp' hash table

#      => (Optional Note: 
#          - you can terminate the usual Bellman Ford algorithm early if there has been no 
#            updates to the shortest weight for any of the nodes in the 'shortest' hash table in an 
#            iteration (you can just track this using a boolean)
#         )

#    - update the 'shortest' hash table with the updated 'temp' hash table

# 3. take the shortest weight for the 'dst' node from the 'shortest' hash table,
#    - if the shortest weight is infinity, return -1 (it is unreachable with at most k stops)
#    - else, return the shortest weight for the 'dst' node from the 'shortest' hash table (it is 
#      reachable with at most k stops)



class Solution:
    def findCheapestPrice(self, n: int, flights: list[list[int]], src: int, dst: int, k: int) -> int:
        # Create the directed weighted graph data structure as an adjacency list
        graph = {}
        for i in range(n):
            graph.update({i : []})

        for i in range(len(flights)):
            graph[flights[i][0]].append((flights[i][2], flights[i][1]))

        # print(graph)


        # Modified Bellman Ford algorithm (due to the at most k stops limit)
        shortest = {}
        for key, value in graph.items():
            if key == src:            
                shortest.update({key : 0})
            else:
                shortest.update({key : float('inf')})

        # print(shortest)
        
        for i in range(k + 1):
            temp = shortest.copy()
            
            for current_node in graph:
                if shortest[current_node] == float('inf'):
                    continue
                
                for weight, neighbour in graph[current_node]:
                    total_weight = shortest[current_node] + weight
                    if total_weight < temp[neighbour]:
                        temp[neighbour] = total_weight

            shortest = temp

        
        if shortest[dst] == float('inf'):
            return -1
        else:
            return shortest[dst]



solution = Solution()
print(solution.findCheapestPrice(4, [[0,1,100],[1,2,100],[2,0,100],[1,3,600],[2,3,200]], 0, 3, 1))      # 700
print(solution.findCheapestPrice(3, [[0,1,100],[1,2,100],[0,2,500]], 0, 2, 1))                          # 200
print(solution.findCheapestPrice(3, [[0,1,100],[1,2,100],[0,2,500]], 0, 2, 0))                          # 500