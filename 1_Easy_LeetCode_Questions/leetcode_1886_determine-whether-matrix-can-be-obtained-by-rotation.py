class Solution:
    def rotateMatrix90degrees(self, mat):
        new_mat = []
        for i in range(len(mat)):
            new_mat.append([])

        # Transpose matrix (swap the columns and rows)
        # Group all elements in terms of their position in their rows
        for i in range(len(mat)):
            for j in range(len(mat[0])):
                new_mat[j].append(mat[i][j])
        print(new_mat)

        # Reverse rows
        new_new_mat = []
        for i in new_mat:
            reversed_i = i[::-1]
            print(f"Not Reversed_i: {i}")
            print(f"Reversed_i: {reversed_i}")
            new_new_mat.append(reversed_i)
        print(f"New new mat: {new_new_mat}")

        return new_new_mat

    def findRotation(self, mat, target):
        if mat == target:
            return True

        for i in range(3):
            mat = self.rotateMatrix90degrees(mat)
            if mat == target:
                return True

        return False
    

solution = Solution()
print(solution.findRotation([[0,1],[1,0]], [[1,0],[0,1]]))                          # true
print(solution.findRotation([[0,1],[1,1]], [[1,0],[0,1]]))                          # false
print(solution.findRotation([[0,0,0],[0,1,0],[1,1,1]], [[1,1,1],[0,1,0],[0,0,0]]))  # true