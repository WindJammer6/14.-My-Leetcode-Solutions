class Solution:

    is_tree = True

    def buildAdjacencyListGraph(self, edges):
        graph = {}

        for i in edges:
            if i[0] not in graph:
                graph.update({i[0] : [i[1]]})
            else:
                graph[i[0]].append(i[1])

            if i[1] not in graph:
                graph.update({i[1] : [i[0]]})
            else:
                graph[i[1]].append(i[0])

        return graph
            
    def dfs_helper(self, start_node, graph, visited, parent):
        # Check if there is any cycle to its parent
        for neighbour in graph[start_node]:
            if (neighbour not in visited):
                visited.append(neighbour)
                print(neighbour)
                self.dfs_helper(neighbour, graph, visited, start_node)
            elif neighbour != parent:
                self.is_tree = False
                print("Cycle Found!")

    def validTree(self, n: int, edges) -> bool:
        if (edges == []) and (n == 1):
            return True

        if (edges == []) and (n > 1):
            return False

        graph = self.buildAdjacencyListGraph(edges)
        print(graph)

        start_node = edges[0][0]

        visited = [start_node]

        print(start_node)
        self.dfs_helper(start_node, graph, visited, -1)
        print(visited)

        if (len(visited) != n) and (self.is_tree == True):
            return False

        return self.is_tree
    

solution = Solution()
print(solution.validTree(5, [[0,1],[0,2],[0,3],[1,4]]))       # true
solution.is_tree = True

print(solution.validTree(5, [[0,1],[1,2],[2,3],[1,3],[1,4]])) # false
solution.is_tree = True

print(solution.validTree(3, [[1,0],[2,0]]))                   # true
solution.is_tree = True