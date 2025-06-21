import java.io.BufferedReader;
import java.io.FileInputStream;
import java.io.IOException;
import java.io.InputStream;
import java.io.InputStreamReader;
import java.util.Arrays;

/**
 * https://www.acmicpc.net/problem/1181
 */
public class Main {

    public static void solution(String[] words) {
        words = Arrays.stream(words).distinct().toArray(String[]::new);
        Arrays.sort(words, (s1, s2) -> {
            int s1Len = s1.length();
            int s2Len = s2.length();

            if (s1Len != s2Len) {
                return Integer.compare(s1.length(), s2.length());
            }
            return s1.compareTo(s2);
        });

        for (String word : words) {
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