# Pseudocode:
# 1. Have a hash table to track if there are any duplicates for each rule for the row, column and grid.
#    If there are duplicates, immediately return false
# 2. If no duplicates found for row, column and grid, return true

class Solution:
    def isValidSudoku(self, board: list[list[str]]) -> bool:
        row_dict = {}
        column_dict = {}
        grid_dict = {}

        # Check rows
        for i in range(len(board)):
            for j in range(len(board[0])):
                # print(row_dict)
                # print(board[i][j])
                if board[i][j] not in row_dict:
                    if board[i][j] != ".": 
                        row_dict.update({board[i][j] : 1})
                else:
                    return False
            row_dict = {}

        # Check columns
        for i in range(len(board)):
            for j in range(len(board[0])):
                # print(column_dict)
                # print(board[j][i])
                if board[j][i] not in column_dict:
                    if board[j][i] != ".": 
                        column_dict.update({board[j][i] : 1})
                else:
                    return False
            column_dict = {}

        # Check grid
        grid_ranges = [
            [(0,2), (0,2)],     # grid 0
            [(3,5), (0,2)],     # grid 1
            [(6,8), (0,2)],     # gird 2
            [(0,2), (3,5)],     # grid 3
            [(3,5), (3,5)],     # grid 4
            [(6,8), (3,5)],     # grid 5
            [(0,2), (6,8)],     # grid 6
            [(3,5), (6,8)],     # grid 7
            [(6,8), (6,8)]      # grid 8
        ]

        for grid_r in grid_ranges:
            for i in range(grid_r[0][0], grid_r[0][1]+1):
                for j in range(grid_r[1][0], grid_r[1][1]+1):
                    # print(grid_dict)
                    # print(board[i][j])
                    if board[i][j] not in grid_dict:   
                        if board[i][j] != ".": 
                            grid_dict.update({board[i][j] : 1})
                    else:
                        return False 
            grid_dict = {}

        return True


solution = Solution()
print(solution.isValidSudoku([["5","3",".",".","7",".",".",".","."],["6",".",".","1","9","5",".",".","."],[".","9","8",".",".",".",".","6","."],["8",".",".",".","6",".",".",".","3"],["4",".",".","8",".","3",".",".","1"],["7",".",".",".","2",".",".",".","6"],[".","6",".",".",".",".","2","8","."],[".",".",".","4","1","9",".",".","5"],[".",".",".",".","8",".",".","7","9"]]))  # True
print(solution.isValidSudoku([["8","3",".",".","7",".",".",".","."],["6",".",".","1","9","5",".",".","."],[".","9","8",".",".",".",".","6","."],["8",".",".",".","6",".",".",".","3"],["4",".",".","8",".","3",".",".","1"],["7",".",".",".","2",".",".",".","6"],[".","6",".",".",".",".","2","8","."],[".",".",".","4","1","9",".",".","5"],[".",".",".",".","8",".",".","7","9"]]))  # False
print(solution.isValidSudoku([[".",".",".",".","5",".",".","1","."],[".","4",".","3",".",".",".",".","."],[".",".",".",".",".","3",".",".","1"],["8",".",".",".",".",".",".","2","."],[".",".","2",".","7",".",".",".","."],[".","1","5",".",".",".",".",".","."],[".",".",".",".",".","2",".",".","."],[".","2",".","9",".",".",".",".","."],[".",".","4",".",".",".",".",".","."]]))  # False