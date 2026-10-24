import java.util.*;
import java.io.*;

class Solution {
    
    int INF = Integer.MAX_VALUE;
    
    public int solution(int N, int[][] roads, int K) {
        List<List<int[]>> graph = new ArrayList<>(N + 1);
        for (int n = 0; n <= N; n++) {
            graph.add(new ArrayList<>());
        }
        for (int[] road : roads) {
            graph.get(road[0]).add(new int[]{road[1], road[2]});
            graph.get(road[1]).add(new int[]{road[0], road[2]});
        }
        
        int st = 1;
        int[] dist = new int[N + 1];
        Arrays.fill(dist, INF);
        dist[st] = 0;
        
        PriorityQueue<int[]> pq = new PriorityQueue<>((a, b) -> Integer.compare(a[0], b[0]));
        pq.offer(new int[]{dist[st], st});
        
        while (!pq.isEmpty()) {
            int[] entry = pq.poll();
            int cost = entry[0];
            int curr = entry[1];
            if (dist[curr] < cost) {
                continue;
            }
            for (int[] next : graph.get(curr)) {
                if (dist[curr] + next[1] < dist[next[0]]) {
                    dist[next[0]] = dist[curr] + next[1];
                    pq.offer(new int[]{dist[next[0]], next[0]});
                }
            }
        }
        
        int ans = 0;
        for (int i = 1; i <= N; i++) {
            if (dist[i] <= K) {
                ans++;
            }
        }
        
        
        return ans;
    }
}