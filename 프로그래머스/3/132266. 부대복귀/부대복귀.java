import java.util.*;
import java.io.*;

class Solution {
    
    public int[] solution(int N, int[][] roads, int[] sources, int destination) {
        List<List<Integer>> graph = new ArrayList<>(N + 1);
        for (int n = 0; n <= N; n++) {
            graph.add(new ArrayList<>());
        }
        for (int[] road : roads) {
            graph.get(road[0]).add(road[1]);
            graph.get(road[1]).add(road[0]);
        }
        

        int[] ans = new int[sources.length];
        for (int i = 0; i < ans.length; i++) {
            int st = sources[i];
            
            int[] dist = new int[N + 1];
            dist[st] = 1;
            ArrayDeque<Integer> dq = new ArrayDeque<>();
            dq.offer(st);

            while (!dq.isEmpty()) {
                int n = dq.poll();
                for (int nn : graph.get(n)) {
                    if (!(dist[nn] == 0)) {
                        continue;
                    }
                    dist[nn] = dist[n] + 1;
                    dq.offer(nn);
                }
            }
            
            if (dist[destination] == 0) {
                ans[i] = -1;
            } else {
                ans[i] = dist[destination] - 1;
            }
        } 
        return ans;
    }
}