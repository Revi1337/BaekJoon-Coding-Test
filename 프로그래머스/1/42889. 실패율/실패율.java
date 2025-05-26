import java.util.*;
import java.util.stream.IntStream;

class Solution {
    
    public int[] solution(int N, int[] stages) {
        int[] stageCount = new int[N + 2];

        for (int s : stages) {
            stageCount[s]++;
        }

        int totalPlayers = stages.length;
        double[] failureRates = new double[N + 1];

        for (int i = 1; i <= N; i++) {
            if (totalPlayers == 0) {
                failureRates[i] = 0;
            } else {
                failureRates[i] = (double) stageCount[i] / totalPlayers;
                totalPlayers -= stageCount[i];
            }
        }

        return IntStream.rangeClosed(1, N)
                .boxed()
                .sorted((i1, i2) -> {
                    int cmp = Double.compare(failureRates[i2], failureRates[i1]);
                    return (cmp != 0) ? cmp : Integer.compare(i1, i2);
                })
                .mapToInt(Integer::intValue)
                .toArray();
    }
}
