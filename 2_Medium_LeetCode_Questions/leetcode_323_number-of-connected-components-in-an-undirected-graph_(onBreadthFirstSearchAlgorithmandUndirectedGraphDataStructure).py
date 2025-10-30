class Solution:
    def build_custom_graph(self, n, edges):
        graph = {}

        for i in range(n):
            graph.update({i : []})

        for i in edges:
            graph[i[0]].append(i[1])
            graph[i[1]].append(i[0])

        return graph
        


    def countComponents(self, n: int, edges):
        graph = self.build_custom_graph(n, edges)
        # print(graph)

        # Breadth First Search algorithm for Graph Data Structure
        queue = []
        visited = []

        visited_nodes = 0
        number_of_connected_components = 0

        for i in range(n):
            if i not in visited:
                queue.append(i)
                number_of_connected_components += 1

                while queue:
                    current_node = queue.pop(0)
                    
                    # print(f"current node: {current_node}")
                    for neighbour in graph[current_node]:
                        if neighbour not in visited:
                            visited.append(neighbour)
                            # print(neighbour)
                            queue.append(neighbour)

                    visited_nodes += 1


        return number_of_connected_components


solution = Solution()
print(solution.countComponents(5, [[0,1],[1,2],[3,4]]))             # 2
print(solution.countComponents(5, [[0,1],[1,2],[2,3],[3,4]]))       # 1