class Solution:
    def setZeroes(self, matrix):
        """
        Do not return anything, modify matrix in-place instead.
        """
        # Identify all rows and columns that needs to be converted to zero
        found_zeros = {"row" : [], "col" : []}

        for row in range(len(matrix)):
            for col in range(len(matrix[0])):
                if matrix[row][col] == 0:

                    if row not in found_zeros["row"]:
                        found_zeros["row"].append(row)

                    if col not in found_zeros["col"]:
                        found_zeros["col"].append(col)

        print(found_zeros)

        # Convert the specified rows and columns to zero
        for row in range(len(matrix)):
            if row in found_zeros["row"]:
                matrix[row] = [0] * len(matrix[0])

        for row in range(len(matrix)):
            for col in range(len(matrix[0])):
                if col in found_zeros["col"]:
                    matrix[row][col] = 0

        print(matrix)


solution = Solution()
print(solution.setZeroes([[1,1,1],[1,0,1],[1,1,1]]))            # [[1,0,1],[0,0,0],[1,0,1]]
print(solution.setZeroes([[0,1,2,0],[3,4,5,2],[1,3,1,5]]))      # [[0,0,0,0],[0,4,5,0],[0,3,1,0]]