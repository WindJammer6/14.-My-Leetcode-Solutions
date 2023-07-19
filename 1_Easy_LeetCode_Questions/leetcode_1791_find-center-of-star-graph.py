class Solution:
    def findCenter(self, edges) -> int:
        one_dimensional_array = []
        dict_counter = {}
        
        for i in edges:
            for j in i:
                one_dimensional_array.append(j)

        for i in one_dimensional_array:
            if i not in dict_counter:
                dict_counter[i] = 1
            else:
                dict_counter[i] += 1

        for index, value in dict_counter.items():
            if value == len(edges):
                return index
        return False

graph = [[1,2],[2,3],[4,2]]

solution = Solution()

print(solution.findCenter(graph))