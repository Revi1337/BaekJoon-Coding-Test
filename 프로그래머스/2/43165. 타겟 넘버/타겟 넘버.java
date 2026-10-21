import java.io.*;
import java.util.*;

class Solution {                            

    int[] numbers;
    int target;
    int ans = 0;
    
    public int solution(int[] numbers, int target) {                            
        this.numbers = numbers;
        this.target = target;
        dfs(0, 0);
        return ans;                  
    }            

    void dfs(int idx, int sum) {
        if (idx == numbers.length) {
            if (sum == target) {
                ans++;
            }
            return;
        }
        dfs(idx + 1, sum + numbers[idx]);
        dfs(idx + 1, sum - numbers[idx]);                    
    }
}
