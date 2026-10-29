# With HEAVY reference to this solution: https://www.youtube.com/watch?v=Ph95IHmRp5M (Neetcode) (YouTube video by Neetcode titled, 
# 'N-Queens - Backtracking - Leetcode 51 - Python')


# Using backtracking, with inspiration to the '17. Letter Combinations of a Phone Number' leetcode 
# question (their codes are very similar as both uses backtracking)


# Pseudocode:
# 1. First we need to understand how a queen can attack another queen. A queen can attack another queen
#    if they are in the same row, column or diagonal line. Hence, no queens can lie on the same row,
#    column or diagonal line as another queen.
# 2. Using backtracking, we try to put a queen on each of the cells in first (every) row.
# 3. Then we try to put a queen on each of the cells in the second row. But we eliminate cells for the 
#    queen in the second row that might cause it to lie on the same column or diagonal line as a queen
#    in the previous rows (we don't need to check for same row because our row by row check already
#    handles this for us)
# 4. Tracking if a previous queen lie in the same column in simple, but how do we track for the diagonal
#    lines? To do this, we check the "posDiag" (positive diagonal, aka bottom left to top right of the 
#    grid) and "negDiag" (negative diagonal, aka top left to bottom right of the grid). 

#    But how does this work, what are the similarity between cells lying on the "posDiag" and "negDiag"?
#    - The pattern of the "posDiag" (/) is that the sum of the row and column (r + c) values which will 
#      always stay the same in the same diagonal line
#             c=0   c=1   c=2   c=3
#            +-----+-----+-----+-----+
#      r=0   |  0  |  1  |  2  |  3  |
#            +-----+-----+-----+-----+
#      r=1   |  1  |  2  |  3  |  4  |
#            +-----+-----+-----+-----+
#      r=2   |  2  |  3  |  4  |  5  |
#            +-----+-----+-----+-----+
#      r=3   |  3  |  4  |  5  |  6  |
#            +-----+-----+-----+-----+
#    - The pattern of the "negDiag" (\) is that the difference between the row and column (r - c) values 
#      which will always stay the same in the same diagonal line
#             c=0   c=1   c=2   c=3
#            +-----+-----+-----+-----+
#      r=0   |  0  | -1  | -2  | -3  |
#            +-----+-----+-----+-----+
#      r=1   |  1  |  0  | -1  | -2  |
#            +-----+-----+-----+-----+
#      r=2   |  2  |  1  |  0  | -1  |
#            +-----+-----+-----+-----+
#      r=3   |  3  |  2  |  1  |  0  |
#            +-----+-----+-----+-----+

#    We cam use this pattern to check if a new queen position is lying in the same "posdiag" and or 
#    "negdiag" as previous queens

# 5. We can track columns or diagonal lines taken up by a previous queen using a "columns", "posDiag"
#    and "negDiag" set


class Solution:
    def solveNQueens(self, n: int) -> list[list[str]]:
        output = []
        columns = set()
        posDiag = set()
        negDiag = set()

        current_puzzle = []
        for i in range(n):
            current_puzzle.append("."*n)
        # print(current_puzzle)

        self.backtracking(0, 0, current_puzzle, n, columns, posDiag, negDiag, output)

        return output


    def backtracking(self, row, column, current_puzzle, n, columns, posDiag, negDiag, output):
        # Base case occurs when all queens have been placed
        if row == n:
            output.append(current_puzzle.copy())
            return

        # Recursive case
        for i in range(n):
            if i not in columns and row - i not in negDiag and row + i not in posDiag:
                columns.add(i)                      # update columns set
                negDiag.add(row - i)                # update "negDiag" set
                posDiag.add(row + i)                # update "posDiag" set
                current_puzzle[row] = current_puzzle[row][:i] + "Q" + current_puzzle[row][i+1:]   # update "current_puzzle" with the new queen position

                # print(current_puzzle)
                self.backtracking(row + 1, i, current_puzzle, n, columns, posDiag, negDiag, output)

                columns.remove(i)                      # undo the added value in the columns set
                negDiag.remove(row - i)                # undo the added value in the "negDiag" set
                posDiag.remove(row + i)                # undo the added value in the "posDiag" set    
                current_puzzle[row] = "."*n            # undo the added new queen position in "current_puzzle"          



solution = Solution()
print(solution.solveNQueens(4))        # [[".Q..","...Q","Q...","..Q."],["..Q.","Q...","...Q",".Q.."]]]
print(solution.solveNQueens(1))        # [["Q"]]