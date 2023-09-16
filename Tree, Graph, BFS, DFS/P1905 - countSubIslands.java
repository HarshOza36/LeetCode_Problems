class Solution {
    public int countSubIslands(int[][] grid1, int[][] grid2) {
        int ans = 0;
        int [][] visited = new int[grid2.length][grid2[0].length];
        

        for(int i = 0; i < grid2.length; i++){
            for(int j = 0; j < grid2[0].length; j++){
                if(visited[i][j] == 0 && grid2[i][j] == 1 && dfs(grid1, grid2, visited, i, j)) ans++;
            }
        }

        return ans;
    }

    public boolean dfs(int[][] grid1, int[][] grid2, int[][] visited, int i, int j){
        if(i < 0 || j < 0 || i >= grid2.length || j >= grid2[0].length || visited[i][j] == 1 || grid2[i][j] == 0){
            return true; // we dont return false because this case doesnt mean its not sub island
        }
        visited[i][j] = 1;
        boolean result = true;
        if(grid1[i][j] == 0) result = false; // it might not be a sub island

        result &= dfs(grid1, grid2, visited, i+1, j);
        result &= dfs(grid1, grid2, visited, i-1, j);
        result &= dfs(grid1, grid2, visited, i, j+1);
        result &= dfs(grid1, grid2, visited, i, j-1);

        // In all 4 directions even if one of the island is missing in grid1, we cannot form a subisland

        return result;
    }
}