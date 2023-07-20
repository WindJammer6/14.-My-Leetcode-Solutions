#'AdjacencyListDirectedGraph' class taken from elsewhere to simulate the Directed Graph Data Structure 
#to create the Directed Graph Data Structure to solve the Leetcode's problem code on
class AdjacencyListDirectedGraph:
    def __init__(self, edges):
        self.edges = edges
        self.graph_dictionary = {}

        for start, end in self.edges:
            if start in self.graph_dictionary:
                self.graph_dictionary[start].append(end)
            else:
                self.graph_dictionary[start] = [end]
            
        for start, end in self.edges:
            if end not in self.graph_dictionary:
                self.graph_dictionary[end] = []

    def add_node(self, node):
        if node in self.graph_dictionary:
            print(node, "is already present in the Graph Data Structure")

        else:
            self.graph_dictionary[node] = []

    def add_edge(self, startnode, endnode):
        if startnode not in self.graph_dictionary:
            print(startnode, "is not present in the Graph Data Structure")
        elif endnode not in self.graph_dictionary:
            print(endnode, "is not present in the Graph Data Structure")

        else:
            self.graph_dictionary[startnode].append(endnode)

    def delete_node(self, node):
        if node not in self.graph_dictionary:
            print(node, "is not present in the Graph Data Structure")

        else:
            self.graph_dictionary.pop(node)
            
            for i in self.graph_dictionary:
                value_list = self.graph_dictionary[i]
                if node in value_list:
                    value_list.remove(node)

    def delete_edge(self, startnode, endnode):
        if startnode not in self.graph_dictionary:
            print(startnode, "is not present in the Graph Data Structure")
        elif endnode not in self.graph_dictionary:
            print(endnode, "is not present in the Graph Data Structure")

        else:
            if endnode in self.graph_dictionary[startnode]:
                self.graph_dictionary[startnode].remove(endnode)
            else:
                print("No such edge exists that is pointing in the direction from", startnode, "to", endnode)

    def breadth_first_search(self, rootnode):
 
        queue_list = []
        visited = []
 
        queue_list.append(rootnode)
 
        while queue_list:
            s = queue_list.pop(0)
            visited.append(s)
            if s in self.graph_dictionary:
                for i in self.graph_dictionary[s]:
                    if i not in visited and i not in queue_list:
                        queue_list.append(i)

        return visited
    
    def depth_first_search(self, rootnode):
 
        stack_list = []
        visited = []
 
        stack_list.insert(0, rootnode)
 
        while stack_list:
            s = stack_list.pop(0)
            visited.append(s)
            if s in self.graph_dictionary:
                for i in self.graph_dictionary[s]:
                    if i not in visited and i not in stack_list:
                        stack_list.insert(0, i)

        return visited
      
    def __repr__(self):
        return '{}'.format(self.graph_dictionary)
    

# Adjacency List Graph Directed Data Structure (for visualisation reference):
# A : [B, C]
# B : [E]
# C : [D]
# D : [B, E]
# E : []


class Solution:
    def findJudge(self, n: int, trust: list[list[int]]) -> int:

        if n == 1:
            return 1
        
        
        trust_graph = AdjacencyListDirectedGraph(trust)
        print(trust_graph)

        potential_town_judge = 0

        for key, value in trust_graph.graph_dictionary.items():
            if value == []:
                potential_town_judge = key
        print(potential_town_judge)


        if potential_town_judge == 0:
            return -1
        

        for key, value in trust_graph.graph_dictionary.items():
            bool_list = []

            if key != potential_town_judge:
                for i in value:
                    if i == potential_town_judge:
                        bool_list.append(True)
                    else:
                        bool_list.append(False)

                if any(bool_list) is False:
                    return -1
                
                print(bool_list)    
                bool_list.clear()
            
        return potential_town_judge
        

trust_list = [[1,2]]

solution = Solution()

print(solution.findJudge(3, trust_list))