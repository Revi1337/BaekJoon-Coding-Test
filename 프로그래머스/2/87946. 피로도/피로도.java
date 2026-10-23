class Solution {
    
    int k;
    int[][] dungeons;
    boolean[] check;
    int ans = 0;

    public int solution(int k, int[][] dungeons) {
        this.k = k;
        this.dungeons = dungeons;
        this.check = new boolean[dungeons.length];
        
        backtrack(0, k, 0);
        
        return this.ans;
    }
    
    public void backtrack(int n, int left, int ans) {
        if (n == dungeons.length) {
            this.ans = Math.max(this.ans, ans);
            return;
        }
        for (int i = 0; i < dungeons.length; i++) {
            if (check[i]) {
                continue;
            }
            check[i] = true;
            if (left >= dungeons[i][0]) {
                backtrack(n + 1, left - dungeons[i][1], ans + 1);
            } else {
                backtrack(n + 1, left, ans);
            }
            check[i] = false;
        }
    }
}