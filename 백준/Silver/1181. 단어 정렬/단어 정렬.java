import java.io.*;
import java.util.*;

/**
 * https://www.acmicpc.net/problem/1181
 */
public class Main {

    public static void solution(String[] words) {
        Set<String> set = new HashSet<>();
        for (int i = 0; i < words.length; i++) {
            set.add(words[i]);
        }

        String[] uniqueWords = set.toArray(new String[0]);
        Arrays.sort(uniqueWords, (s1, s2) -> {
            if (s1.length() != s2.length()) {
                return Integer.compare(s1.length(), s2.length());
            }
            return s1.compareTo(s2);
        });

        StringBuilder sb = new StringBuilder();
        for(String s : uniqueWords){
            sb.append(s).append('\n');
        }
        System.out.println(sb);
    }

    public static void main(String[] args) throws IOException {
        InputStream input = System.in;
        BufferedReader br = new BufferedReader(new InputStreamReader(input));

        int N = Integer.parseInt(br.readLine());
        String[] words = br.lines().limit(N).toArray(String[]::new);
        solution(words);
    }
}