# With HEAVY reference to this solution: https://www.youtube.com/watch?v=6kTZYvNNyps (Neetcode) (YouTube video by Neetcode 
# titled, 'Alien Dictionary - Topological Sort - Leetcode 269 - Python')

# Pseudocode:
# 1. Determine the different orderings based on the first differing letter between each pair of words, and build a directed 
#    unweighted graph data structure based on these different orderings
# 2. Do Topological Sort (using either DFS or BFS) on the directed unweighted graph data structure
# 3. If there is a cycle, then the ordering is invalid


class Solution:
    def alienOrder(self, words):
        # 1. Building the directed unweighted graph data structure using the different orderings which is based on the 
        #    first differing letter between each pair of words
        graph = {}
        for word in words:
            for letter in word:
                if letter not in graph:
                    graph.update({letter : []})
        print(graph)

        
        for i in range(len(words) - 1):
            min_length = len(min([words[i], words[i+1]], key=len))
            for j in range(min_length):
                if words[i][j] == words[i+1][j]:
                    pass
                else:
                    graph[words[i][j]].append(words[i+1][j])
                    break

            # Handling the edge case where if the second word is the prefix of the first order, then the order immediately invalid 
            # (e.g. 'ape' comes before 'apes' or 'apple' comes before 'app', when it is supposed to be the other way around instead)
            if len(words[i]) > len(words[i+1]) and words[i][:min_length] == words[i+1][:min_length]:
                return ""

        print(graph)     


        # 2. Doing Topological Sort using DFS on the directed unweighted graph data structure
        # 3. If there is a cycle, then the ordering is invalid
        #    - use the 3 state system to detect if there is a cycle
        stack = []
        visited = {}

        for currentnode in graph.keys():
            visited.update({currentnode : 0})
        print(visited)

        for key, value in graph.items():
            if visited[key] == 0:
                if self.dfs_helper(graph, visited, key, stack):
                    return ""                               # Cycle detected — ordering is invalid
        print(stack)

        stack.reverse()
        output = ""
        for i in stack:
            output += i
        return output


    def dfs_helper(self, graph, visited, currentnode, stack):
        visited[currentnode] = 1            # Mark as in-progress
        for neighbour in graph[currentnode]:
            if visited[neighbour] == 1:
                return True                 # Back-edge — cycle detected
            if visited[neighbour] == 0:
                if self.dfs_helper(graph, visited, neighbour, stack):
                    return True             # Propagate cycle upward
        
        visited[currentnode] = 2
        stack.append(currentnode)
        return False                        # No cycle detected — ordering is valid
    


solution = Solution()
print(solution.alienOrder(["wrt","wrf","et","ett","rftt"]))         # ""tfwer""
print(solution.alienOrder(["z","x"]))                               # "zx"
print(solution.alienOrder(["z","x","z"]))                           # ""
print(solution.alienOrder(["wrt","wrf","er","ett","rftt"]))         # "wertf"
print(solution.alienOrder(["z","z"]))                               # "z"