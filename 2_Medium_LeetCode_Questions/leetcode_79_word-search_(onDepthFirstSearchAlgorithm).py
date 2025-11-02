class Solution:

    found_word = False

    def dfs(self, board, word, visited, marker, target_index, current_row, current_column):
        if (0 <= current_row < len(board)) and (0 <= current_column < len(board[0])) and (target_index < len(word)):
            if (board[current_row][current_column] == word[target_index]):
                visited.append(board[current_row][current_column])
                marker[current_row][current_column] = 1
                
                visited_string = ''.join(visited)
                # print(word)
                # print(visited_string)
                # print(marker)
                if word == visited_string:
                    self.found_word = True
                
                if (0 <= current_row + 1 < len(board)):
                    if (marker[current_row + 1][current_column] == 0):
                        self.dfs(board, word, visited, marker, target_index + 1, current_row + 1, current_column)
                if (0 <= current_row - 1 < len(board)):
                    if marker[current_row - 1][current_column] == 0: 
                        self.dfs(board, word, visited, marker, target_index + 1, current_row - 1, current_column)
                if (0 <= current_column + 1 < len(board[0])):
                    if marker[current_row][current_column + 1] == 0: 
                        self.dfs(board, word, visited, marker, target_index + 1, current_row, current_column + 1)
                if (0 <= current_column - 1 < len(board[0])):
                    if marker[current_row][current_column - 1] == 0: 
                        self.dfs(board, word, visited, marker, target_index + 1, current_row, current_column - 1)

                visited.pop()
                marker[current_row][current_column] = 0                

        


    def exist(self, board, word):

        visited = []
        marker = []
        for i in range(len(board)):
            marker.append([0] * len(board[0]))

        # Search the board, if found first letter of the word to find, then start DFS
        for row in range(len(board)):
            for col in range(len(board[0])):
                # Do DFS
                self.dfs(board, word, visited, marker, 0, row, col)
                visited = []
                marker = []
                for i in range(len(board)):
                    marker.append([0] * len(board[0]))

                if self.found_word == True:
                    return True

        return False
    

solution = Solution()
solution.found_word = False
print(solution.exist([["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], "ABCCED"))              # true              
solution.found_word = False
print(solution.exist([["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], "SEE"))                 # true
solution.found_word = False
print(solution.exist([["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], "ABCB"))                # false
solution.found_word = False
print(solution.exist([["A","B","C","E"],["S","F","E","S"],["A","D","E","E"]], "ABCESEEEFS"))          # true