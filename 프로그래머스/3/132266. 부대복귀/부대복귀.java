import java.util.*;
import java.io.*;

class Solution {
    
    int INF = Integer.MAX_VALUE;
    
    public int[] solution(int N, int[][] rds, int[] srcs, int dst) {
        List<List<Integer>> graph = new ArrayList<>(N + 1);
        for (int n = 0; n <= N; n++) {
            graph.add(new ArrayList<>());
        }
        for (int[] rd : rds) {
            graph.get(rd[0]).add(rd[1]);
            graph.get(rd[1]).add(rd[0]);   
        }
        
        int[] dist = new int[N + 1];
        Arrays.fill(dist, INF);
        dist[dst] = 0;

        PriorityQueue<int[]> pq = new PriorityQueue<>((a, b) -> Integer.compare(a[0], b[0]));
        pq.offer(new int[]{dist[dst], dst});

        while (!pq.isEmpty()) {
            int[] entry = pq.poll();
            int c = entry[0];
            int n = entry[1];
            if (dist[n] < c) {
                continue;
            }
            for (int nn : graph.get(n)) {
                if (dist[n] + 1 < dist[nn]) {
                    dist[nn] = dist[n] + 1;
                    pq.offer(new int[]{dist[nn], nn});
                }
            }
        }
        
        int[] ans = new int[srcs.length];
        for (int idx = 0; idx < srcs.length; idx++) {
            int st = srcs[idx];
            if (dist[st] == INF) {
                ans[idx] = -1;
            } else {
                ans[idx] = dist[st];
            }
        }
        return ans;
    }
}

// import java.util.*;
// import java.io.*;

// class Solution {
    
//     public int[] solution(int N, int[][] roads, int[] sources, int destination) {
//         List<List<Integer>> graph = new ArrayList<>(N + 1);
//         for (int n = 0; n <= N; n++) {
//             graph.add(new ArrayList<>());
//         }
//         for (int[] road : roads) {
//             graph.get(road[0]).add(road[1]);
//             graph.get(road[1]).add(road[0]);
//         }
        

//         int[] ans = new int[sources.length];
//         for (int i = 0; i < ans.length; i++) {
//             int st = sources[i];
            
//             int[] dist = new int[N + 1];
//             dist[st] = 1;
//             ArrayDeque<Integer> dq = new ArrayDeque<>();
//             dq.offer(st);

//             while (!dq.isEmpty()) {
//                 int n = dq.poll();
//                 for (int nn : graph.get(n)) {
//                     if (!(dist[nn] == 0)) {
//                         continue;
//                     }
//                     dist[nn] = dist[n] + 1;
//                     dq.offer(nn);
//                 }
//             }
            
//             if (dist[destination] == 0) {
//                 ans[i] = -1;
//             } else {
//                 ans[i] = dist[destination] - 1;
//             }
//         } 
//         return ans;
//     }
// }