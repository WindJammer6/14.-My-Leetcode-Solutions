# With HEAVY reference to this solution: https://www.youtube.com/watch?v=f7JOBJIC-NA (Neetcode) (YouTube video by Neetcode titled, 
# 'Prim's Algorithm - Minimum Spanning Tree - Min Cost to Connect all Points - Leetcode 1584 - Python')


# What is a Minimum Spanning Tree (MST)?
# Its literally what this leetcode question is asking you to find. A Minimum Spanning Tree (MST) is a 
# subset of edges in a weighted undirected graph that connects all the vertices together without any 
# cycles (acyclic) and with the minimum possible total edge weight. 

# Source: https://www.geeksforgeeks.org/dsa/what-is-minimum-spanning-tree-mst/ (GeekforGeeks)


# What is the Prim's algorithm, Kruskal's algorithm and Boruvka's algorithm (as per the leetcode question
# topics)?
# All 3 of these algorithms fundamentally solve the same fundamental problem, which is to find a Minimum 
# Spanning Tree (MST) of a weighted undirected graph. They differ in how they grow the tree and what data 
# structures they rely on. But for the sake of solving leetcode questions, we can simply stick to one of 
# them. Neetcode recommends sticking to Prim's algorithm as it is the easiest to understand.


# Pseudocode (basically Prim's algorithm):
# Prim's algorithm is similar to Dijkstra's algorithm (which allows you to find the shortest path 
# distances from the source vertex to all other vertices in the graph).

# 1. Initialize 2 data structures, a 'visited' hash set and a 'frontier' min-heap, and a 'cost' variable
# 2. First construct the weighted undirected Graph Data Structure, where the nodes are the points and
#    the edges are the path from each node to all other nodes. The weight/cost of these edges is the
#    manhattan distance between 2 nodes.
# 3. Starting from any node and adding this starting node into the 'frontier' min-heap, and while length 
#    of 'visited' is less that number of nodes (we will only terminate Prim's algorithm when all nodes 
#    have been 'visited'):
#    - Pop the root node in the 'frontier' min-heap, as this will be the node with the smallest cost to
#      our current Minimum Spanning Tree (MST), and add this node to 'visited' so we do not revisit it
#      again and create a cycle in the MST
#    - Add all of the neighbours to the 'frontier' min-heap that is not already in 'visited' in the format:
#           [cost, node]

#    - IMPORTANT NOTE: Note that during this process, the 'frontier' min-heap might contain multiple
#      elements with the same node. What happens when the root node that we popped from the 'frontier' 
#      min-heap is already in 'visited'? In this case, we just ignore it, and we keep popping until we
#      find a new popped root node that is not yet in 'visited')



import heapq

class Solution:
    def minCostConnectPoints(self, points: list[list[int]]) -> int:
        # Create the weighted undirected Graph Data Structure as an adjacency list
        graph = {}

        for i in range(len(points)):
            for j in range(i+1, len(points)):
                if i not in graph:
                    graph.update({i : [(abs(points[i][0] - points[j][0]) + abs(points[i][1] - points[j][1]), j)]})
                else:
                    graph[i].append((abs(points[i][0] - points[j][0]) + abs(points[i][1] - points[j][1]), j))

                if j not in graph:
                    graph.update({j : [(abs(points[i][0] - points[j][0]) + abs(points[i][1] - points[j][1]), i)]})
                else:
                    graph[j].append((abs(points[i][0] - points[j][0]) + abs(points[i][1] - points[j][1]), i))

        # print(graph)


        # Prim's algorithm
        visited = set()
        min_heap = []
        min_cost = 0

        starting_node = (0, 0)
        heapq.heappush(min_heap, starting_node)

        while len(visited) < len(points):
            cost, node = heapq.heappop(min_heap)
            while node in visited:
                cost, node = heapq.heappop(min_heap)

            min_cost += cost
            visited.add(node)
            if graph:
                for i in graph[node]:
                    if i[1] not in visited:
                        heapq.heappush(min_heap, i)
                # print(visited)

        return min_cost



solution = Solution()
print(solution.minCostConnectPoints([[0,0],[2,2],[3,10],[5,2],[7,0]]))    # 20
print(solution.minCostConnectPoints([[3,12],[-2,5],[-4,1]]))              # 18
print(solution.minCostConnectPoints([[0,0]]))                             # 0