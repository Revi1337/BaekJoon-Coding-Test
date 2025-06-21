import java.io.*;
import java.util.*;

/**
 * https://www.acmicpc.net/problem/1181
 */
public class Main {

    public static void solution(int N, String[] words) {
        Arrays.sort(words, (s1, s2) -> {
            if (s1.length() != s2.length()) {
                return Integer.compare(s1.length(), s2.length());
            }
            return s1.compareTo(s2);
        });
        
        StringBuilder sb = new StringBuilder();
        sb.append(words[0]).append('\n');
        for(int i = 1; i < N; i ++) {
            if(!words[i].equals(words[i - 1])) {
                sb.append(words[i]).append('\n');
            }
        }
        System.out.println(sb);
    }

    public static void main(String[] args) throws IOException {
        InputStream input = System.in;
        BufferedReader br = new BufferedReader(new InputStreamReader(input));

        int N = Integer.parseInt(br.readLine());
        String[] words = br.lines().limit(N).toArray(String[]::new);
        solution(N, words);
    }
}