class Solution:
    def spiralOrder(self, matrix):
        n = len(matrix)
        
        # Setting boundaries (indexes here are inclusive)
        up = -1
        down = n
        left = -1
        right = len(matrix[0])

        current_direction = "right" 
        current_row = 0
        current_column = 0
        spiral_order = [matrix[0][0]]

        while (down - 1> up) and (right - 1> left):
            print(f"Direction: {current_direction}")
            print(spiral_order)

            print(f"Curr row: {current_row}")
            print(f"Curr column: {current_column}")

            print(f"Up: {up}")
            print(f"down: {down}")
            print(f"left: {left}")
            print(f"right: {right}")

            if current_direction == "right":
                for i in range(current_column + 1, right):
                    print(i)
                    spiral_order.append(matrix[current_row][i])
                up += 1
                current_column = right - 1

            elif current_direction == "down":
                for i in range(current_row + 1, down):
                    print(i)
                    spiral_order.append(matrix[i][current_column])
                right -= 1
                current_row = down - 1

            elif current_direction == "left":
                for i in range(current_column - 1, left, -1):
                    print(i)
                    spiral_order.append(matrix[current_row][i])
                down -= 1
                current_column = left + 1

            else:   # up
                for i in range(current_row - 1, up, -1):
                    print(i)
                    spiral_order.append(matrix[i][current_column])
                left += 1
                current_row = up + 1

            # Change direction
            if current_direction == "right":
                current_direction = "down"
            elif current_direction == "down":
                current_direction = "left"
            elif current_direction == "left":
                current_direction = "up"
            else:   # up
                current_direction = "right"

            print(spiral_order)

        return spiral_order
    

solution = Solution()
print(solution.spiralOrder([[1,2,3],[4,5,6],[7,8,9]]))              # [1,2,3,6,9,8,7,4,5]
print(solution.spiralOrder([[1,2,3,4],[5,6,7,8],[9,10,11,12]]))     # [1,2,3,4,8,12,11,10,9,5,6,7]