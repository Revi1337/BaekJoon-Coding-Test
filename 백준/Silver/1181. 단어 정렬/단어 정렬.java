import java.io.*;
import java.util.*;

/**
 * https://www.acmicpc.net/problem/1181
 */
public class Main {

    public static void solution(String[] words) {
        Set<String> set = new HashSet<>(Arrays.asList(words));
        String[] uniqueWords = set.toArray(new String[0]);
        Arrays.sort(uniqueWords, (s1, s2) -> {
            int s1Len = s1.length();
            int s2Len = s2.length();

            if (s1Len != s2Len) {
                return Integer.compare(s1.length(), s2.length());
            }
            return s1.compareTo(s2);
        });

        for (String word : uniqueWords) {
            System.out.println(word);
        }
    }

    public static void main(String[] args) throws IOException {
        InputStream input = System.in;
        BufferedReader br = new BufferedReader(new InputStreamReader(input));

        int N = Integer.parseInt(br.readLine());
        String[] words = br.lines().limit(N).toArray(String[]::new);
        solution(words);
    }
}