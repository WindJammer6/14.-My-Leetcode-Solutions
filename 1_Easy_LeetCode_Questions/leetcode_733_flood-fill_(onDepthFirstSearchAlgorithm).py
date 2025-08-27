class Solution:
    def floodFill(self, image, sr, sc, color):
        if color == image[sr][sc]:
            return image

        visited = []

        color_to_match = image[sr][sc]
        image[sr][sc] = color
        self.dfs(image, sr, sc, visited, color, color_to_match)

        return image

    def dfs(self, image, x, y, visited, color, color_to_match):
        directions = [(+1, 0), (-1, 0), (0, +1), (0, -1)]
        for direct in directions:
            cur_x, cur_y = x + direct[0], y + direct[1]
            if (0 <= cur_x < len(image)) and (0 <= cur_y < len(image[0])) and ((cur_x, cur_y) not in visited) and (image[cur_x][cur_y] == color_to_match):
                visited.append((cur_x, cur_y))
                image[cur_x][cur_y] = color
                self.dfs(image, cur_x, cur_y, visited, color, color_to_match)

solution = Solution()
print(solution.floodFill([[1,1,1],[1,1,0],[1,0,1]], 1, 1, 2))   # [[2,2,2],[2,2,0],[2,0,1]]
print(solution.floodFill([[0,0,0],[0,0,0]], 0, 0, 0))           # [[0,0,0],[0,0,0]]