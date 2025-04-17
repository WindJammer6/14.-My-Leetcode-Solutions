class Solution:

    # Direction vectors
    dRow = [-1, 0, 1, 0]
    dCol = [ 0, 1, 0, -1]


    # With reference to one of the solutions on Leetcode, following the approach:
    # Source: https://leetcode.com/problems/number-of-islands/solutions/6650299/bfs/?envType=problem-list-v2&envId=oizxjoit (Leetcode) 
    #         (a Leetcode solution to this question)
    # 1. keep a count variable.
    # 2. traverse over matrix.
    # 3. if grid[i][j] == '1':
    #    apply bfs.(mark all the visited cell as visited by making all visited land cell as water cell.)
    #    increment count variable.
    def numIslands(self, grid):
        island_counter = 0

        # Create the 'visited' 2D array
        vis = []
        for i in range(len(grid)):
            vis.append([])
            for j in range(len(grid[0])):
                vis[i].append(False)

        # Iterate through the grid normally
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == "1":
                    island_counter += 1
                    self.BFS_modified(grid, vis, i, j)

        return island_counter
 


    # Initial Breadth First Search (BFS) on a 2D array code from GeekforGeeks. This is a slightly modified BFS to
    # answer this question's context by me, according to the approach of one of the solutions to this question on 
    # Leetcode.
    # Source: https://www.geeksforgeeks.org/breadth-first-traversal-bfs-on-a-2d-array/ (GeeksforGeeks) (BFS on a 
    #         2D array code from GeekforGeeks)

    # Function to check if a cell
    # is be visited or not
    def isValid(self, vis, row, col, row_limit, col_limit):
    
        # If cell lies out of bounds
        if (row < 0 or col < 0 or row >= row_limit or col >= col_limit):
            return False
    
        # If cell is already visited
        if (vis[row][col]):
            return False
    
        # Otherwise
        return True
    
    # Function to perform the BFS traversal
    def BFS_modified(self, grid, vis, row, col):
        # Stores indices of the matrix cells
        q = []
    
        # Mark the starting cell as visited
        # and push it into the queue
        q.append(( row, col ))
        vis[row][col] = True
    
        # Iterate while the queue
        # is not empty
        while (len(q) > 0):
            cell = q.pop(0)
            x = cell[0]
            y = cell[1]
    
            #q.pop()
    
            # Go to the adjacent cells
            for i in range(4):
                adjx = x + self.dRow[i]
                adjy = y + self.dCol[i]
                if (self.isValid(vis, adjx, adjy, len(grid), len(grid[0])) and (grid[adjx][adjy] == "1")):
                    q.append((adjx, adjy))
                    vis[adjx][adjy] = True
                    grid[adjx][adjy] = "0"
            



grid1 = [
  ["1","1","1","1","0"],
  ["1","1","0","1","0"],
  ["1","1","0","0","0"],
  ["0","0","0","0","0"]
]

grid2 = [
  ["1","1","0","0","0"],
  ["1","1","0","0","0"],
  ["0","0","1","0","0"],
  ["0","0","0","1","1"]
]

solution = Solution()
print(solution.numIslands(grid1))   # 1
print(solution.numIslands(grid2))   # 3