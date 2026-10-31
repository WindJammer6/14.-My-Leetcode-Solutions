# With inspiration from the number of islands leetcode question (as their codes are very similar)


class Solution:
    def dfs(self, start, grid):
        # up down left right
        directions = [[-1, 0], [1,0], [0,-1], [0,1]]
        area_of_island = 1

        stack = []
        stack.append(start)
        grid[start[0]][start[1]] = 0

        while stack:
            current = stack.pop()
            # print(current)
            for i in range(4):
                # Check if the neighbour is within bounds and is part of an island
                if 0 <= current[0] + directions[i][0] < len(grid) and 0 <= current[1] + directions[i][1] < len(grid[0]) and grid[current[0] + directions[i][0]][current[1] + directions[i][1]] == 1:
                    stack.append([current[0] + directions[i][0], current[1] + directions[i][1]])
                    grid[current[0] + directions[i][0]][current[1] + directions[i][1]] = 0
                    area_of_island += 1

        return area_of_island


    def maxAreaOfIsland(self, grid: list[list[int]]) -> int:
        max_area = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    area_of_island = self.dfs([i, j], grid)
                    # print(area_of_island)
                    if area_of_island > max_area:
                        max_area = area_of_island

        return max_area



solution = Solution()
print(solution.maxAreaOfIsland([[0,0,1,0,0,0,0,1,0,0,0,0,0],[0,0,0,0,0,0,0,1,1,1,0,0,0],[0,1,1,0,1,0,0,0,0,0,0,0,0],[0,1,0,0,1,1,0,0,1,0,1,0,0],[0,1,0,0,1,1,0,0,1,1,1,0,0],[0,0,0,0,0,0,0,0,0,0,1,0,0],[0,0,0,0,0,0,0,1,1,1,0,0,0],[0,0,0,0,0,0,0,1,1,0,0,0,0]]))    # 6
print(solution.maxAreaOfIsland([[0,0,0,0,0,0,0,0]]))          # 0