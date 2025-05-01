class Solution:
    def splitWordsBySeparator(self, words, separator: str):
        result_list = []

        for word in words:
            index_stopped_at = 0

            for i in range(len(word)):
                if word[i] == separator:
                    if word[index_stopped_at : i] != "":
                        result_list.append(word[index_stopped_at : i])
                    index_stopped_at = i+1

            if index_stopped_at != len(word):
                result_list.append(word[index_stopped_at : len(word)])

        return result_list

        
solution = Solution()
print(solution.splitWordsBySeparator(["one.two.three","four.five","six"], "."))     # ["one","two","three","four","five","six"]
print(solution.splitWordsBySeparator(["$easy$","$problem$"], "$"))                  # ["easy","problem"]
print(solution.splitWordsBySeparator(["|||"], "|"))                                 # []