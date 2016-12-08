public class Solution {
    public int calculateMinimumHP(int[][] dungeon) {
        int row = dungeon.length;
        int col = dungeon[0].length;
        int healthGrid[][] = new int [row][col];
        healthGrid[row - 1][col - 1] = Math.max(1, 1 - dungeon[row - 1][col - 1]);
        for (int i = row - 2; i >= 0; i--) {
            healthGrid[i][col - 1] = Math.max(1, healthGrid[i + 1][col - 1] - dungeon[i][col - 1]);
        }
        for (int i = col - 2; i >= 0; i--) {
            healthGrid[row - 1][i] = Math.max(1, healthGrid[row - 1][i + 1] - dungeon[row - 1][i]);
        }
        for (int i = row - 2; i >= 0; i--) {
            for (int j = col - 2; j >= 0; j--) {
                healthGrid[i][j] = Math.max(1, Math.min(healthGrid[i + 1][j], healthGrid[i][j + 1]) - dungeon[i][j]);
            }
        }
        return healthGrid[0][0];
    }
}
