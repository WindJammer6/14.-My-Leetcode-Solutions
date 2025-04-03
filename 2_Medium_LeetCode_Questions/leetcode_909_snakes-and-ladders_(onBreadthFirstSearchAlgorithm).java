import java.util.ArrayList;

public class TestSolution {
    public static void main(String[] args){
        Solution solution = new Solution();

        int[][] board1 = {
                {-1,-1,-1,-1,-1,-1},
                {-1,-1,-1,-1,-1,-1},
                {-1,-1,-1,-1,-1,-1},
                {-1,35,-1,-1,13,-1},
                {-1,-1,-1,-1,-1,-1},
                {-1,15,-1,-1,-1,-1}};
        System.out.println(solution.snakesAndLadders(board1));  // 4

        int[][] board2 = {
                {-1,-1},
                {-1,3}};
        System.out.println(solution.snakesAndLadders(board2));  // 1

        int[][] board3 = {
                {-1,-1,-1},
                {-1, 9, 8},
                {-1, 8, 9}};
        System.out.println(solution.snakesAndLadders(board3));  // 1 ✅ Now correct
    }
}

class Solution {

    public static class Cell {
        int x, y, minDis;
        Cell(int x, int y, int minDis) {
            this.x = x;
            this.y = y;
            this.minDis = minDis;
        }

        Cell(int x, int y) {
            this(x, y, 0);
        }
    }

    public int snakesAndLadders(int[][] board) {
        int n = board.length;
        Cell[] labelMap = buildLabelMap(board);
        Cell start = labelMap[1];

        boolean[] visited = new boolean[n * n + 1];
        return BFS(board, visited, start, labelMap);
    }


    // Idea to solve this question is doing Breadth-First Search (BFS) algorithm
    // through a 2D-array/matrix
    // Source: https://www.geeksforgeeks.org/breadth-first-traversal-bfs-on-a-2d-array/ (GeekforGeeks)

    // Pseudocode:
    // 1. Initialize the direction vectors dRow[] = {-1, 0, 1, 0} and dCol[] = {0, 1, 0, -1}
    //    and a queue of pairs to store the indices of matrix cells.
    // 2. Start BFS traversal from the first cell, i.e. (0, 0), and enqueue the index of this cell
    //    into the queue.
    // 3. Initialize a boolean array to mark the visited cells of the matrix. Mark the cell (0, 0) as
    //    visited.
    // 4. Declare a function isValid() to check if the cell coordinates are valid or not, i.e lies
    //    within the boundaries of the given Matrix and are unvisited or not.
    // 5. Iterate while the queue is not empty and perform the following operations:
    //      5a. Dequeue the cell present at the front of the queue and print it.
    //      5b. Move to its adjacent cells that are not visited.
    //      5c. Mark them visited and enqueue them into the queue.
    private int BFS(int[][] board, boolean[] visited, Cell start, Cell[] labelMap) {
        int n = board.length;
        int destination = n * n;

        ArrayList<Cell> queue = new ArrayList<>();
        queue.add(new Cell(start.x, start.y, 0));
        visited[1] = true;

        while (!queue.isEmpty()) {
            Cell current = queue.remove(0);
            int currentLabel = getLabel(labelMap, current);

            if (currentLabel == destination) {
                return current.minDis;
            }

            for (int i = 1; i <= 6; i++) {
                int nextLabel = currentLabel + i;
                if (nextLabel > destination) break;

                Cell next = labelMap[nextLabel];
                int r = next.x, c = next.y;

                int destLabel = board[r][c] != -1 ? board[r][c] : nextLabel;

                if (!visited[destLabel]) {
                    visited[destLabel] = true;
                    Cell destCell = labelMap[destLabel];
                    queue.add(new Cell(destCell.x, destCell.y, current.minDis + 1));
                }
            }
        }

        return -1;
    }

    private Cell[] buildLabelMap(int[][] board) {
        int n = board.length;
        Cell[] map = new Cell[n * n + 1];
        boolean leftToRight = true;
        int label = 1;

        for (int row = n - 1; row >= 0; row--) {
            if (leftToRight) {
                for (int col = 0; col < n; col++) {
                    map[label++] = new Cell(row, col);
                }
            } else {
                for (int col = n - 1; col >= 0; col--) {
                    map[label++] = new Cell(row, col);
                }
            }
            leftToRight = !leftToRight;
        }
        return map;
    }

    private int getLabel(Cell[] labelMap, Cell cell) {
        for (int i = 1; i < labelMap.length; i++) {
            if (labelMap[i].x == cell.x && labelMap[i].y == cell.y) {
                return i;
            }
        }
        return -1; // should not happen
    }
}
