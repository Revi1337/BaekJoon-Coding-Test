import java.util.*;

class Solution {
    
    int[] drow = {-1, 0, 1, 0};
    int[] dcol = {0, 1, 0, -1};
    
    public int solution(int[][] maps) {
        int n = maps.length;
        int m = maps[0].length;
        int answer = 0;

        int[][] dist = new int[n][m];
        Deque<int[]> dq = new ArrayDeque<>();
        dist[0][0] = 1;
        dq.offer(new int[]{0, 0});
        
        while (!dq.isEmpty()) {
            int[] entry = dq.poll();
            int row = entry[0];
            int col = entry[1];
            for (int d = 0; d < 4; d++) {
                int nrow = row + drow[d];
                int ncol = col + dcol[d];
                if (nrow < 0 || nrow >= n || ncol < 0 || ncol >= m) {
                    continue; 
                }
                if (maps[nrow][ncol] == 0 || dist[nrow][ncol] != 0){
                    continue;
                }
                dq.offer(new int[]{nrow, ncol});
                dist[nrow][ncol] = dist[row][col] + 1;
            }
        }
        
        return dist[n - 1][m - 1] == 0 ? -1 : dist[n - 1][m - 1];
    }
}