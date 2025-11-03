class Solution:
    def build_directed_graph(self, numCourses, prerequisites):
        graph = {}
        for i in range(numCourses):
            graph.update({i : []})

        for prerequisite in prerequisites:
            graph[prerequisite[1]].append(prerequisite[0])

        print(graph)
        return graph

    def dfs_helper(self, currentnode, graph, visited, recStack):
        # If the node is already in the current recursion stack, a cycle is detected
        if recStack[currentnode] == True:
            return True

        # If the node is already visited and not part of the recursion stack, skip it
        if visited[currentnode] == True:
            return False

        visited[currentnode] = True
        recStack[currentnode] = True

        for neighbour in graph[currentnode]:
            if self.dfs_helper(neighbour, graph, visited, recStack) == True:
                return True

        # Remove the node from the recursion stack before returning
        recStack[currentnode] = False
        return False

    # With reference to this:
    # - https://www.geeksforgeeks.org/dsa/detect-cycle-in-a-graph/ (GeekforGeeks)
    def canFinish(self, numCourses: int, prerequisites: list[list[int]]) -> bool:
        graph = self.build_directed_graph(numCourses, prerequisites)

        # Doing DFS (the goal is to use DFS to check if there is a cycle in the Directed Graph Data Structure. If there is a cycle, then you cannot finish all courses, else you can finish all courses).
        visited = [False] * numCourses
        recStack = [False] * numCourses         # To track vertices in the current DFS path

        for i in range(numCourses):
            if self.dfs_helper(i, graph, visited, recStack) == True:
                return False

        return True


solution = Solution()
print(solution.canFinish(2, [[1,0]]))                       # True
print(solution.canFinish(2, [[1,0],[0,1]]))                 # False
print(solution.canFinish(5, [[1,4],[2,4],[3,1],[3,2]]))     # True