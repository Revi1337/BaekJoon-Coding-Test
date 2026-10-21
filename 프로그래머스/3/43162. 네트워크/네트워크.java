import java.util.*;

class Solution {

    public int solution(int n, int[][] computers) {
        int answer = 0;
        boolean[] check = new boolean[n];
        Deque<Integer> queue = new ArrayDeque<>();
        
        for (int c = 0; c < computers.length; c++) {
            if (!check[c]) {
                answer++;
                check[c] = true;
                queue.offer(c);
                
                while (!queue.isEmpty()) {
                    int curr = queue.poll();
                    for (int next = 0; next < n; next++) {
                        if (computers[curr][next] == 1 && !check[next]) {
                            check[next] = true;
                            queue.offer(next);
                        } 
                    }
                }
            }
        }
        
        return answer;
    }
}