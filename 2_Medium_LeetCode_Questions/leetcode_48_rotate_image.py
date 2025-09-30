class Solution:
    def rotate(self, matrix):
        """
        Do not return anything, modify matrix in-place instead.
        """
        # Transpose matrix in place (swap the columns and rows)
        for i in range(len(matrix)):
            for j in range(i, len(matrix[0])):
                if i != j:
                    temp = matrix[i][j]
                    # print(temp)
                    # print("Before")
                    # print(matrix[j][i])
                    # print(matrix[i][j])
                    matrix[i][j] = matrix[j][i]
                    matrix[j][i] = temp
                    # print("After")
                    # print(matrix[j][i])
                    # print(matrix[i][j])
                    
        print(matrix)

        # Reverse rows in place
        n = len(matrix[0])
        if n % 2 == 0:   # Even
            middle_index = n // 2
            print(middle_index)
            for i in range(len(matrix)):
                for j in range(middle_index):
                    print("Before")
                    print(matrix[i])
                    temp = matrix[i][j]
                    matrix[i][j] = matrix[i][n - 1 - j]
                    matrix[i][n - 1 - j] = temp
                    print("After")
                    print(matrix[i])
        
        else:                   # Odd
            middle_index = n // 2
            print(middle_index)
            for i in range(len(matrix)):
                for j in range(middle_index):
                    print("Before")
                    print(matrix[i])
                    temp = matrix[i][j]
                    matrix[i][j] = matrix[i][n - 1 - j]
                    matrix[i][n - 1 - j] = temp
                    print("After")
                    print(matrix[i])


        print(matrix)


matrix1 = [[1,2,3],[4,5,6],[7,8,9]]
matrix2 = [[5,1,9,11],[2,4,8,10],[13,3,6,7],[15,14,12,16]]

solution = Solution()

solution.rotate(matrix1)
print(matrix1)      # [[7,4,1],[8,5,2],[9,6,3]]

solution.rotate(matrix2)
print(matrix2)      # [[15,13,2,5],[14,3,4,1],[12,6,8,9],[16,7,10,11]]