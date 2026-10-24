import java.util.*;

class Solution {
    
    int[] parent;

    public int solution(int N, int[][] computers) {
        parent = new int[N + 1];
        for (int p = 1; p <= N; p++) {
            parent[p] = p;
        }
        
        for (int i = 0; i < N; i++) {
            for (int j = i + 1; j < N; j++) {
                if (computers[i][j] == 1) {
                    union(i, j);
                }
            }
        }
        
        int answer = 0;
        for (int i = 0; i < N; i++) {
            if (find(i) == i) {
                answer++;
            }
        }
        return answer;
    }
    
    int find(int n) {
        if (parent[n] == n) {
            return n;
        }
        parent[n] = find(parent[n]);
        return parent[n];
    }
    
    boolean union(int n1, int n2) {
        int r1 = find(n1);
        int r2 = find(n2);
        if (r1 == r2) {
            return false;
        }
        parent[r1] = r2;
        return true;
    }
    
}


// import java.util.*;

// class Solution {

//     public int solution(int n, int[][] computers) {
//         int answer = 0;
//         boolean[] check = new boolean[n];
//         Deque<Integer> queue = new ArrayDeque<>();
        
//         for (int c = 0; c < computers.length; c++) {
//             if (!check[c]) {
//                 answer++;
//                 check[c] = true;
//                 queue.offer(c);
                
//                 while (!queue.isEmpty()) {
//                     int curr = queue.poll();
//                     for (int next = 0; next < n; next++) {
//                         if (computers[curr][next] == 1 && !check[next]) {
//                             check[next] = true;
//                             queue.offer(next);
//                         } 
//                     }
//                 }
//             }
//         }
        
//         return answer;
//     }
// }