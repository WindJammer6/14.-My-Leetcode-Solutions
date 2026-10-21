# With HEAVY reference to this solution: https://www.youtube.com/watch?v=Akt3glAwyfY (Neetcode) (YouTube 
# video by Neetcode titled, 'Course Schedule II - Topological Sort - Leetcode 210')


# Note that Topological Sort algorithm only works on a Directed Acyclic Graph (DAG),
# recall that it does not work on undirected or cyclic graphs! It however, can work
# for disjointed graphs.

# It is impossible to finish all courses when a cycle is detected.

class Solution:
    def topological_sort_via_recursive_dfs(self, current, graph, visited, cycle, output):
        # Base cases
        if current in cycle:            # Cycle detected
            return False
        if current in visited:          # Don't need visit again, but you don't want to terminate the
            return True                 # algorithm

        cycle.add(current)
        for neighbour in graph[current]:
            if self.topological_sort_via_recursive_dfs(neighbour, graph, visited, cycle, output) is False:
                return False
        
        cycle.remove(current)
        visited.add(current)
        output.append(current)

        return True


    def findOrder(self, numCourses: int, prerequisites: list[list[int]]) -> list[int]:
        # Creating the Directed Acyclic Graph (DAG)
        graph = {}
        for i in range(numCourses):
            graph.update({i : []})

        for i in prerequisites:
            graph[i[1]].append(i[0])

        # print(graph)

        visited = set()
        cycle = set()
        result = []

        # To factor in disjointed graphs
        for i in range(numCourses):
            if self.topological_sort_via_recursive_dfs(i, graph, visited, cycle, result) is False:
                return []

        result = result[::-1]

        return result



solution = Solution()
print(solution.findOrder(2, [[1,0]]))                       # [0,1]
print(solution.findOrder(4, [[1,0],[2,0],[3,1],[3,2]]))     # [0,2,1,3]
print(solution.findOrder(1, []))                            # [0]