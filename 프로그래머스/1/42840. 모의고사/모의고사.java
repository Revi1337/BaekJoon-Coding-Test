import java.util.*;

class Solution {
    public int[] solution(int[] answers) {
        int[] result = new int[3];
        
        int[][] pattern = {
            {1,2,3,4,5},
            {2,1,2,3,2,4,2,5},
            {3,3,1,1,2,2,4,4,5,5,3,3,1,1,2,2,4,4,5,5}
        };
        
        for (int i = 0; i < answers.length; i++) {
            for (int j = 0; j < pattern.length; j++) {
                if (answers[i] == pattern[j][i % pattern[j].length]) {
                    result[j] += 1;
                }
            }
        }
        
        int mx = Arrays.stream(result).max().getAsInt();
        ArrayList<Integer> lst = new ArrayList<>();
        for (int i = 0; i < result.length; i++) {
            if (result[i] == mx) {
                lst.add(i + 1);
            }
        }
        
        return lst.stream().mapToInt(Integer::intValue).toArray();
    }
}
