public class Solution {
    public int minPathSum(int[][] grid) {
        int row = grid.length;
        int col = grid[0].length;
        for (int i = 0; i < row - 1; i++) {
            grid[i+1][0] += grid[i][0];
        }
        for (int i = 0; i < col - 1; i++) {
            grid[0][i+1] += grid[0][i];
        }
        for (int i = 1; i < row; i++) {
            for (int j = 1; j < col; j++) {
                grid[i][j] += grid[i][j-1] > grid[i-1][j] ? grid[i-1][j] : grid[i][j-1];
            }
        }
        return grid[row-1][col-1];
    }
}
