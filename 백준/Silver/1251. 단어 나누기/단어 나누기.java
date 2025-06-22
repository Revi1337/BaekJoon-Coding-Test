import java.io.*;
import java.util.*;

/**
 * https://www.acmicpc.net/problem/1251
 */
public class Main {

    public static String solution(String word) {
        int length = word.length();
        ArrayList<String> lst = new ArrayList<>();
        for (int i = 1; i < length - 2; i++) {
            for (int j = i + 1; j < length; j++) {
                StringBuilder sb = new StringBuilder();
                sb.append(new StringBuilder(word.substring(0, i)).reverse());
                sb.append(new StringBuilder(word.substring(i, j)).reverse());
                sb.append(new StringBuilder(word.substring(j)).reverse());
                lst.add(sb.toString());
            }
        }

        Collections.sort(lst);

        return lst.get(0);
    }

    public static void main(String[] args) throws IOException {
        InputStream input = System.in;
        BufferedReader br = new BufferedReader(new InputStreamReader(input));

        String word = br.readLine();
        System.out.println(solution(word));
    }
}
