import heapq


# Approach 1: Using Dijsktra's Algorithm and Adjacency List Directed Weighted Data Structure (dosen't work, misunderstood the question)
# What is the misunderstanding?
# My Dijkstra algorithm's structure are fundamentally correct for problems with static edge weights. However, Leetcode 3341 introduces 
# dynamic weights based on time constraints (moveTime), which invalidates the static graph model. To solve such time-aware problems, 
# Dijkstra must be adapted to compute transition costs dynamically at runtime, which this approach's graph abstraction does not support.

# ❓ What I Assumed:
# - That each move from one cell to an adjacent cell:
#   -> Costs 0 if not the final destination, or 1 if it is.
#   -> Can be made immediately, without waiting.
# - That the moveTime[i][j] value is only important for the final cell.
# - That edge weights can be precomputed and fixed before running Dijkstra.

# ✅ What the Problem Actually Requires:
# - Every move to a neighbor cell always costs at least 1 second (the base move).
# - If you arrive at a cell before its moveTime[i][j], you must wait until the allowed time — meaning the true cost depends on when you arrive.
# - So, the effective cost to move to a cell is dynamic, and must be computed at runtime, not during graph construction.


# Approach:
# 1. Build the 2D matrix/array of size n x m, as an Adjacency List Directed Graph Data 
#    Structure
# 2. Run Dijsktra's Algorithm on this Adjacency List Directed Graph Data 
#    Structure, to find shortest path from the source vertex to every 
#    other vertex in the graph.
# 3. Return the shortest path from the source vertex to the last vertex, where
#    (n - 1, m - 1)

class AdjacencyListDirectedWeightedDataStructure:
    def __init__(self, edges):
        self.edges = edges
        self.graph_dictionary = {}

        for start, end, cost in self.edges:
            if start in self.graph_dictionary:
                self.graph_dictionary[start].append((end, cost))

            else:
                self.graph_dictionary[start] = [(end, cost)]

        for start, end in self.edges:
            if end not in self.graph_dictionary:
                self.graph_dictionary[end] = []


    def add_node(self, node):
        if node in self.graph_dictionary:
            print(node, "is already present in the Graph Data Structure")

        else:
            self.graph_dictionary[node] = []


    def add_edge(self, startnode, endnode, cost):
        if startnode not in self.graph_dictionary:
            print(startnode, "is not present in the Graph Data Structure")
        elif endnode not in self.graph_dictionary:
            print(endnode, "is not present in the Graph Data Structure")
        else:
            tuple = (endnode, cost)
            self.graph_dictionary[startnode].append(tuple)

    #So I can use the 'print()' function on my 'AdjacencyListDirectedGraph' class to look at my 
    #'AdjacencyListDirectedGraph' object
    def __repr__(self):
        return '{}'.format(self.graph_dictionary)



    # Using Dijsktra's Algorithm, with the following approach from W3Schools:
    # Source:
    # - https://www.w3schools.com/dsa/dsa_algo_graphs_dijkstra.php (W3Schools)

    # Approach:
    # 1. Set initial distances for all vertices: 0 for the source vertex, and infinity for all the other.
    # 2. Choose the unvisited vertex with the shortest distance from the start to be the current vertex. So the algorithm 
    #    will always start with the source as the current vertex.
    # 3. For each of the current vertex's unvisited neighbor vertices, calculate the distance from the source and update 
    #    the distance if the new, calculated, distance is lower.
    # 4. We are now done with the current vertex, so we mark it as visited. A visited vertex is not checked again.
    # 5. Go back to step 2 to choose a new current vertex, and keep repeating these steps until all vertices are visited.
    # 6. In the end we are left with the shortest path from the source vertex to every other vertex in the graph.

    # Pseudocode (from my university's notes):
    # Let 𝐺 = (𝑉, 𝐸) be a weighted directed graph, let 𝑠 be a vertex of
    # 𝐺, and let 𝑤: 𝐸 → ℝ be the weight function of 𝐺.
    # - Assume: Every vertex 𝑣 of 𝐺 has two attributes 𝑣.𝑑 and 𝑣.𝜋
    #   -> 𝑣.𝑑 represents an estimate of the value of 𝛿(𝑠, 𝑣).
    #   -> 𝑣.𝜋 represents the parent of the vertex 𝑣 in a shortest-paths tree

    # function Dijkstra(𝐺, 𝑤, 𝑠):
    # Require: A weight function 𝑤 for 𝐺. A vertex 𝑠 of 𝐺.
    # Require: A directed graph 𝐺 represented as an adjacency list,
    # where 𝐺. 𝐴𝑑𝑗[𝑢] is the linked list of vertices adjacent to 𝑢.
    # 1. initialize_single-source(𝐺, 𝑠)
    # 2. 𝑆 ← ∅                  # Initialize S as an empty set
    # 3. 𝑄 ← 𝐺. 𝑉               # Here, Q is a min-priority queue. The elements of Q are vertices, and the keys of these elements are the d values
    # 4. while 𝑄 ≠ ∅:
    # 5.    𝑢 ← extract_min(𝑄)  # 𝑢 has the smallest 𝑑 value among the vertices in 𝑄, and it is removed from 𝑄.
    # 6.    𝑆 ← 𝑆 ∪ {𝑢}
    # 7.    for each vertex 𝑣 ∈ 𝐺. 𝐴𝑑𝑗[𝑢]:
    # 8.        relax(𝑢, 𝑣, 𝑤)

    # function relax(𝑢, 𝑣, 𝑤, Q):
    # Require: (𝑢, 𝑣) is a directed edge of 𝐺.
    # Require: Q is a min-priority queue. The elements of Q are vertices, and the keys of these elements are the d values.
    # 1. if 𝑢.𝑑 + 𝑤(𝑢, 𝑣) < 𝑣.𝑑 then:
    # 2.     𝑣.𝑑 ← 𝑢.𝑑 + 𝑤(𝑢, 𝑣)
    # 3.     𝑣.𝜋 ← u
    # 4.     update Q             # Re-prioritize v in the priority queue

    # function initialize_single-source(𝐺, 𝑠):
    # Require: 𝐺 = (𝑉, 𝐸) is a weighted directed graph.
    # Require: 𝑠 ∈ 𝑉 is a vertex
    # 1. for every vertex 𝑣 ∈ 𝑉:
    # 2.     𝑣.𝑑 ← ∞
    # 3.     𝑣.𝜋 ← NIL
    # 4. 𝑠.𝑑 ← 0
    def initialize_single_source(self, start_vertex):
        distances = {}
        for vertex in self.graph_dictionary:
            distances[vertex] = 100000000000000000
        
        predecessor = {}
        for vertex in self.graph_dictionary:
            predecessor[vertex] = None

        # Set distance of source vertex as 0
        distances[start_vertex] = 0

        # The distances and predecessor dictionaries should look something like this before running Dijsktra's algorithm:
        #       distance = {
        #           0: 0,
        #           1: inf,
        #           2: inf,
        #           3: inf
        #       }
        #       predecessor = {
        #           0: None,
        #           1: None,
        #           2: None,
        #           3: None
        #       }
        return distances, predecessor
            

    def relax(self, current_vertex, neighbour_vertex, weight, distances, predecessor, priority_queue_data_structure):
        if distances[current_vertex] + weight < distances[neighbour_vertex]:
            distances[neighbour_vertex] = distances[current_vertex] + weight
            predecessor[neighbour_vertex] = current_vertex
            heapq.heappush(priority_queue_data_structure, (distances[neighbour_vertex], neighbour_vertex))


    def dijsktra_algorithm(self, start_vertex):
        distances, predecessor = self.initialize_single_source(0)
        finalised_set = set()
        priority_queue_data_structure = []
        # The priority queue data structure should look something like this, where the first element is
        # distance and second is the vertex '(distance, vertex)':
        #       [(0, 0), (3, 1), (7, 2)]

        # Why can't I let it be '(vertex, distance)' instead?
        # From ChatGPT:
        # You can make your priority queue tuples (vertex, distance) — but you’ll break 'heapq' library's behavior 
        # unless you manually tell Python how to prioritize them.

        # ⚠️ Why (vertex, distance) doesn’t work directly with heapq
        # By default, heapq always prioritizes the first element in a tuple:
        #           heapq.heappush(heap, (first, second))
        # It orders by first.

        # ❌ So if you use (vertex, distance), it will prioritize vertex ID, not distance!
        # Example:
        #       heap = []
        #       heapq.heappush(heap, (5, 1))  # vertex 5, distance 1
        #       heapq.heappush(heap, (1, 10)) # vertex 1, distance 10

        # Then:
        #       heapq.heappop(heap) → (1, 10)  # WRONG: node 1 has worse distance, but comes first


        # Start by pushing the start vertex with distance 0 
        heapq.heappush(priority_queue_data_structure, (start_vertex, 0))

        while len(priority_queue_data_structure) != 0:
            _, vertex_with_smallest_d_value = heapq.heappop(priority_queue_data_structure)
            finalised_set.add(vertex_with_smallest_d_value)
            for neighbour_vertex in self.graph_dictionary[vertex_with_smallest_d_value]:
                self.relax(vertex_with_smallest_d_value, neighbour_vertex[0], neighbour_vertex[1], distances, predecessor, priority_queue_data_structure) 
        

        # The distances dictionaries should look something like this after running Dijsktra's algorithm:
        #       distance = {
        #           0: 0,
        #           1: 2,
        #           2: 2,
        #           3: 5
        #       }

        #       predecessor = {
        #           0: None,
        #           1: 0,
        #           2: 0,
        #           3: 1
        #       }
        print(distances)
        print(predecessor)

        return distances
            
        
class Solution1:
    def minTimeToReach1(self, moveTime):
        # Number each cell with an identifier number
        moveTime_identifier = []
        counter = 0
        for row in range(len(moveTime)):
            moveTime_identifier.append([])
            # print(row)
            for column in range(len(moveTime[row])):
                moveTime_identifier[row].append(counter)
                counter += 1

        # print(moveTime_identifier)
        
        # Construct Adjacency List Directed Weighted Graph Data Structure
        graph = AdjacencyListDirectedWeightedDataStructure([])
        for i in range(len(moveTime)):
            for j in range(len(moveTime[0])):
                node_id = moveTime_identifier[i][j]
                graph.add_node(node_id)

        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]     # up, down, left, right
        for i in range(len(moveTime)):
            for j in range(len(moveTime[0])):
                from_id = moveTime_identifier[i][j]

                for direction_x, direction_y in directions:
                    new_i, new_j = i + direction_x, j + direction_y
                    if 0 <= new_i < len(moveTime) and 0 <= new_j < len(moveTime[0]):
                        to_id = moveTime_identifier[new_i][new_j]
                        
                        # Only add moveTime cost if the target is not the final cell
                        to_id = moveTime_identifier[new_i][new_j]
                        final_node_id = len(moveTime) * len(moveTime[0]) - 1

                        if to_id == final_node_id:
                            cost = 1
                        else:
                            cost = 1 + moveTime[new_i][new_j]
                        
                        graph.add_edge(from_id, to_id, cost)
        
        # Print Adjacency List Directed Weighted Graph Data Structure
        print(graph)

        shortest_distances_from_sources_vertex_to_all_vertices = graph.dijsktra_algorithm(0)

        # Return the shortest path from the source vertex to the last vertex, where
        # (n - 1, m - 1), from the returned output 'distances' dictionary
        return shortest_distances_from_sources_vertex_to_all_vertices[len(moveTime) * len(moveTime[0]) - 1]
    

# ///////////////////////////////////////////////////////////////////////////////////


# Approach 2: Using modified Dijsktra's Algorithm (works) (Generated by ChatGPT because I gave up after coming up with Approach 1)

# Explanation of the code by ChatGPT:
# Question: How did this code do Dijsktra's Algorithm without a Grpah Data Structure?

# Your current Solution2 does indeed implement Dijkstra’s algorithm, but instead of building a separate graph data structure 
# (like an adjacency list), it directly uses the grid as the graph.

# 🧠 How Dijkstra Still Works Without an Explicit Graph

# ✅ Dijkstra’s Core Requirements
# Dijkstra's algorithm only needs:
# 1. A way to store distances (shortest time so far to each node).
# 2. A way to get neighbors of a node.
# 3. A priority queue to always process the node with the smallest distance so far.

# ✅ What You Did Instead of a Graph
# | Typical Graph Dijkstra                               | Your Grid-Based Version                           |
# | ---------------------------------------------------- | ------------------------------------------------- |
# | Store nodes in `graph[node] = [(neighbor, cost), …]` | Use 2D grid cells `(i,j)` as nodes                |
# | Loop over `graph[u]` to get neighbors                | Loop over `[(dx,dy)]` to get neighbors of `(x,y)` |
# | Maintain a dictionary `dist[node]`                   | Use `distance[i][j]` 2D list                      |
# | Use `heapq` to extract min-distance node             | Same! You do this correctly                       |

# So the grid itself is the graph.
# - Each cell is a node.
# - Each valid adjacent move (up/down/left/right) is an edge with dynamic cost.
# - The cost of moving to (nx, ny) is computed on-the-fly based on:
#   -> Time it takes to move (+1)
#   -> Required wait time if arrival < moveTime[nx][ny].

# 🔁 Analogy
# | Concept             | Classic Graph  | Grid Implementation                        |
# | ------------------- | -------------- | ------------------------------------------ |
# | Node                | Vertex `v`     | Cell `(x, y)`                              |
# | Neighbors           | `graph[v]`     | `[(x+dx, y+dy) for dx,dy]`                 |
# | Edge weight         | `w(u, v)`      | `max(moveTime[nx][ny], curr_time + 1) + 1` |
# | Distance            | `dist[v]`      | `distance[x][y]`                           |
# | Priority queue item | `(dist, node)` | `(time, x, y)`                             |


# ✅ Why This Still Is Dijkstra
# Because:
# - You always expand the unvisited node with the smallest time (heapq).
# - You update distance only if a better time is found.
# - Each node is finalized only once with its shortest arrival time.

# All of this matches Dijkstra’s semantics — the only difference is that the graph is implicit.

class GridDijkstra:
    def __init__(self, moveTime):
        self.grid = moveTime
        self.n = len(moveTime)
        self.m = len(moveTime[0])
        self.directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

    def initialize_single_source(self):
        distance = [[float('inf')] * self.m for _ in range(self.n)]
        distance[0][0] = 0
        return distance

    def relax(self, x, y, nx, ny, curr_time, distance, pq):
        # We may have to wait until moveTime[nx][ny]
        leave_time = max(curr_time, self.grid[nx][ny])
        arrive_time = leave_time + 1            # <-- add the missing +1

        if arrive_time < distance[nx][ny]:
            distance[nx][ny] = arrive_time
            heapq.heappush(pq, (arrive_time, nx, ny))

    def dijkstra(self):
        distance = self.initialize_single_source()
        pq = [(0, 0, 0)]  # (time, x, y)

        while pq:
            curr_time, x, y = heapq.heappop(pq)

            if curr_time > distance[x][y]:
                continue

            if x == self.n - 1 and y == self.m - 1:
                return curr_time

            for dx, dy in self.directions:
                nx, ny = x + dx, y + dy
                if 0 <= nx < self.n and 0 <= ny < self.m:
                    self.relax(x, y, nx, ny, curr_time, distance, pq)

        return -1
    
class Solution2:
    def minTimeToReach2(self, moveTime):
        solver = GridDijkstra(moveTime)
        return solver.dijkstra()




solution = Solution1()
print(solution.minTimeToReach1([[0,4],[4,4]]))       # 6
print(solution.minTimeToReach1([[0,0,0],[0,0,0]]))   # 3
print(solution.minTimeToReach1([[0,1],[1,2]]))       # 3
print(solution.minTimeToReach1([[17,56],[97,80]]))   # 58       # Fails as Approach 1 gives output of 81 instead

solution = Solution2()
print(solution.minTimeToReach2([[0,4],[4,4]]))       # 6
print(solution.minTimeToReach2([[0,0,0],[0,0,0]]))   # 3
print(solution.minTimeToReach2([[0,1],[1,2]]))       # 3
print(solution.minTimeToReach2([[17,56],[97,80]]))   # 58